from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth
from Monitor.models.Plan.Plan import Plan
from Monitor.models.UserPlan.UserPlan import UserPlan
from Monitor.utils import decrypt_data


class AddPlanInfoWithID(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        plan_id = request.data['deviceCode'][45:-45]
        openid = request.user.openid
        plan = Plan.objects.filter(planid=plan_id).first()
        # up, created = UserPlan.objects.get_or_create(openid=openid, plan_id=plan_id)
        if plan:
            if plan.useTime > 0:
                plan.useTime -= 1
                plan.save()
                up, created = UserPlan.objects.get_or_create(openid=openid, plan_id=plan_id)
                if created:
                    return JsonResponse({
                        # 'data': {
                        #     'devices': [
                        #         {'result': "success",
                        #          'id': 'savePhoneNumber',
                        #          'name': '智能灌溉系统',
                        #          "updateTime": '1717398223000',
                        #          'active': 1,
                        #          'icon': 'GG'}],
                        # }
                        'device': [
                            {
                             'id': plan.planid,
                             'name': plan.name,
                             "updateTime": plan.updateTime,
                             'active': plan.active,
                             'icon': plan.icon}, ],
                        'result': "success",
                    })
                else:  # 设备全部添加完成
                    return JsonResponse({
                        'result': "have",
                    })
            else:
                return JsonResponse({
                    'result': "no",
                })
        else:
            return JsonResponse({
                'result': "fail",
            })

# def get_plan(request, encrypted_id):
#     # 查询并解密
#     plan = Plan.objects.get(planid=encrypted_id)
#     decrypted_id = decrypt_data(plan.planid)
#
#     return JsonResponse({
#         "id": decrypted_id,
#         "name": plan.name,
#         "use_time": plan.useTime
#     })
