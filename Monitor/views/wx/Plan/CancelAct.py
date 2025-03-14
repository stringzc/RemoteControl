from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth
from Monitor.models.Plan.Plan import Plan


class CancelAct(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        planid = request.data['PlanId']
        plan = Plan.objects.filter(planid=planid).first()
        if plan:
            command = '11000'
            cache_key = 'ACT'
            data = cache.get(cache_key)
            if data is None:
                return JsonResponse({
                    'status': 1
                })
            else:
                cache.delete(cache_key)
                device_id = plan.plan_device
                # 通过WebSocket发送指令
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    device_id,
                    {
                        "type": "send_command",
                        "message": command
                    }
                )
                return JsonResponse({
                    'status': 0
                })
        else:
            return JsonResponse({
                'status': 999
            })
