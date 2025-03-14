from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth
from Monitor.models.PlanTime.PlanTime import PlanTime
from Monitor.models.Plan.Plan import Plan

class SaveAutoRecords(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def post(self, r):
        records = r.data['records']
        plan = Plan.objects.filter(planid=r.data['PlanId']).first()
        if plan:
            for _ in records:
                pt = PlanTime.objects.create(Plan_id=plan, StartTime=_['startTime'], EndTime=_['endTime'])
            return JsonResponse({"result": 'success'})
        else:
            return JsonResponse({"result": 'fail'})
