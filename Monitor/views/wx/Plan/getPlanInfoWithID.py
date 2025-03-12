from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from Monitor.models.UserPlan.UserPlan import UserPlan
from Monitor.models.Plan.Plan import Plan

from Monitor.authentication import TokenAuth


class getPlanInfoWithID(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        openid = request.user.openid
        plan = UserPlan.objects.filter(openid=openid)
        devices = []
        if plan:
            for i in plan:
                j = Plan.objects.get(planid=i.plan_id)
                if j:
                    devices.append(
                        {
                            'id': j.planid,
                            'name': j.name,
                            "updateTime": j.updateTime,
                            'active': j.active,
                            'icon': j.icon
                        }
                    )
            return JsonResponse({
                'devices': devices,
                'result': "success"
            }, )
        else:
            return JsonResponse({
                'devices': devices,
                'result': "fail"
            })
