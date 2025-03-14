from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth
from Monitor.models.PlanTime.PlanTime import PlanTime


class getAutoTimeWithPlanID(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def post(self, r):
        PlanId = r.data['PlanId']
        AuToTime = PlanTime.objects.filter(Plan_id=PlanId)
        if AuToTime:
            records = []
            for _ in AuToTime:
                records.append({
                    'start_time': _.StartTime,
                    'end_time': _.EndTime
                })
            return JsonResponse({"result": 'success', "data": records})
        else:
            return JsonResponse({"result": 'fail'})
