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
        plan_id = request.data['deviceCode'][45:90]
        openid = request.user.openid
        plan = Plan.objects.all()
        up, created = UserPlan.objects.get_or_create(openid=openid, plan_id=plan_id)
        if created:
            decrypted_plan_id = None
            for i in plan:
                decrypted_id = decrypt_data(i.planid)
                if plan_id == decrypted_id:
                    decrypted_plan_id = i
            if decrypted_plan_id.useTime > 0:
                decrypted_plan_id.useTime -= 1
                decrypted_plan_id.save()
                up.plan_id = decrypted_plan_id.planid
                up.save()
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
                         'id': decrypted_plan_id.planid,
                         'name': decrypted_plan_id.name,
                         "updateTime": decrypted_plan_id.updateTime,
                         'active': decrypted_plan_id.active,
                         'icon': decrypted_plan_id.icon}, ],
                    'result': "success",
                })
            else:  # 设备全部添加完成
                return JsonResponse({
                    'result': "fail",
                })
        else:
            return JsonResponse({
                'result': "have",
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
