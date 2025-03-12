from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth


class PlanAct(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print(request.data['PlanId'])
        print(request, type(request))
        return JsonResponse({
            'status': 0
        })
