from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth


class getAutoTimeWithPlanID(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def post(self, r):
        records = [
            {"start_time": "08:00", "end_time": "10:00"},
            {"start_time": "14:00", "end_time": "16:00"}
        ]
        return JsonResponse({"code": 200, "data": records})
