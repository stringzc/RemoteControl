from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ControlConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device_id = None

    async def connect(self):
        # 获取设备号并作为房间名的一部分
        print(123321)
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        room_group_name = self.device_id

        # 加入房间
        await self.channel_layer.group_add(
            room_group_name,
            self.channel_name
        )

        # 接受 WebSocket 连接
        await self.accept()

    async def disconnect(self, close_code):
        # 离开房间
        await self.channel_layer.group_discard(
            f"device_{self.device_id}",
            self.channel_name
        )

    async def receive(self, text_data):
        # 可选：接收来自设备的消息
        message = '123'
        await self.send(text_data=message)

    # 向房间组内发送消息
    async def send_command(self, event):
        # 从事件中获取消息并发送给设备
        message = event['message']
        print(f"Sending message: {message}")  # 打印待发送的消息
        await self.send(text_data=message)
