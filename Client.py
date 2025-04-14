
import asyncio
import json
import logging
import traceback
import websockets
from datetime import datetime
from backoff import expo, on_exception

# 配置参数
DJANGO_WS_URL = "wss://www.aurage.cn/wss/ControlConsumer/raspberry_001/"
RECONNECT_INTERVAL = 5
MAX_RECONNECT_ATTEMPTS = 10
PING_INTERVAL = 10
PING_TIMEOUT = 15

# 初始化日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("RaspberryPi")


class ConnectionManager:
    """异步安全连接管理器"""

    def __init__(self):
        self.websocket = None
        self._connected = asyncio.Event()
        self._lock = asyncio.Lock()
        self._is_manually_closed = False
        self.receive_queue = asyncio.Queue()
        self.send_queue = asyncio.Queue()

    @property
    def connected(self):
        return self._connected.is_set()

    async def maintain_connection(self):
        """连接保活主循环"""
        while not self._is_manually_closed:
            try:
                async with self._lock:
                    if self.websocket:
                        await self.websocket.close()

                    self.websocket = await websockets.connect(
                        DJANGO_WS_URL,
                        ping_interval=PING_INTERVAL,
                        ping_timeout=PING_TIMEOUT,
                        close_timeout=1
                    )
                    self._connected.set()
                    logger.info("WebSocket连接成功")

                    # 启动收发任务
                    await asyncio.gather(
                        self._keep_receiving(),
                        self._keep_sending(),
                        self._heartbeat()
                    )

            except Exception as e:
                logger.error(f"连接异常: {str(e)}")
                await self._safe_close()
                await asyncio.sleep(RECONNECT_INTERVAL)

    async def _keep_receiving(self):
        """持续接收消息"""
        try:
            while self.connected:
                message = await self.websocket.recv()
                await self.receive_queue.put(message)
                logger.debug(f"接收消息: {message}")
        except websockets.ConnectionClosed:
            logger.warning("连接已关闭")
            await self._safe_close()
        except Exception as e:
            logger.error(f"接收错误: {str(e)}")
            await self._safe_close()

    async def _keep_sending(self):
        """持续发送消息"""
        try:
            while self.connected:
                data = await self.send_queue.get()
                if self.connected:
                    await self.websocket.send(json.dumps(data))
                    logger.info(f"发送成功: {data}")
        except websockets.ConnectionClosed:
            await self._safe_close()
        except Exception as e:
            logger.error(f"发送错误: {str(e)}")
            await self._safe_close()

    async def _heartbeat(self):
        """心跳检测"""
        try:
            while self.connected:
                await asyncio.sleep(PING_INTERVAL)
                if self.connected:
                    await self.websocket.ping()
                    logger.debug("心跳检测正常")
        except Exception as e:
            logger.error(f"心跳异常: {str(e)}")
            await self._safe_close()

    async def _safe_close(self):
        """安全关闭连接"""
        async with self._lock:
            if self.connected:
                self._connected.clear()
                try:
                    await self.websocket.close()
                except:
                    pass
                finally:
                    self.websocket = None
                    logger.warning("连接已安全关闭")


async def data_generator(manager):
    """模拟数据生成器"""
    while True:
        try:
            data = {
                "status": "1",
                "updateTime": datetime.now().strftime("%Y/%m/%d %H-%M-%S")
            }
            await manager.send_queue.put(data)
            await asyncio.sleep(10)
        except Exception as e:
            logger.error(f"数据生成异常: {str(e)}")


async def data_processor(manager):
    """数据处理器"""
    while True:
        try:
            message = await manager.receive_queue.get()
            logger.info(f"开始处理消息: {message}")

            # 添加具体业务逻辑
            try:
                data = json.loads(message)
                logger.info(f"解析成功: {data}")
                # 示例响应处理
                if data.get("command"):
                    response = {"status": "received", "command": data["command"]}
                    await manager.send_queue.put(response)
            except json.JSONDecodeError:
                logger.warning("收到非JSON格式数据")

        except Exception as e:
            logger.error(f"处理异常: {str(e)}")


async def main():
    manager = ConnectionManager()

    # 启动核心任务
    main_tasks = asyncio.gather(
        manager.maintain_connection(),
        data_generator(manager),
        data_processor(manager)
    )

    try:
        await main_tasks
    except asyncio.CancelledError:
        logger.info("正在关闭服务...")
        manager._is_manually_closed = True
        await manager._safe_close()
        logger.info("服务已安全退出")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("用户中断服务")
