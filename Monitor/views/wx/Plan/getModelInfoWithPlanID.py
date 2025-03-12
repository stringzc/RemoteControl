from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth


class getModelInfoWithPlanID(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def post(self, r):
        Model = [
            {"id": "1", "name": "1", 'description': "打开将给一号区域土地供水",
             'imageUrl': 'https://img95.699pic.com/photo/40242/7819.jpg_wh860.jpg'},
            {"id": "2", "name": "2", 'description': "打开将给二号区域土地供水",
             'imageUrl': 'https://img95.699pic.com/photo/40242/7819.jpg_wh860.jpg'},
        ]
        return JsonResponse({"data": Model})
