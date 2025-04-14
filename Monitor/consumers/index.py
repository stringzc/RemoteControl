from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from Monitor.models.Plan.Plan import Plan


class ControlConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device_id = None

    async def connect(self):
        # 获取设备号并作为房间名的一部分
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
            self.device_id,
            self.channel_name
        )

    @database_sync_to_async
    def db_get_player(self):
        try:
            return Plan.objects.filter(plan_device=self.device_id).first()
        except Plan.DoesNotExist:
            return None

    @database_sync_to_async
    def update_plan_status(self, plan, status, updateTime):
        """更新Plan状态"""
        plan.active = status  # 假设字段名为plan_device_status
        plan.updateTime = updateTime
        plan.save()  # 仅更新必要字段

    async def receive(self, text_data):
        # 可选：接收来自设备的消息
        try:
            data = json.loads(text_data)
            status = data.get("status")
            if status:

                plan = await self.db_get_player()
                if not plan:
                    await self.send(text_data="Error: Plan not found for this device")
                    return
                await self.update_plan_status(plan, status)
                # await self.send(text_data="Status updated successfully")
        except json.JSONDecodeError:
            await self.send(text_data="Error: Invalid JSON format")
        except Exception as e:
            await self.send(text_data=f"Error: {str(e)}")
        # message = '123'
        # await self.send(text_data=message)

    # 向房间组内发送消息
    async def send_command(self, event):
        # 从事件中获取消息并发送给设备
        message = event['message']
        await self.send(text_data=message)
