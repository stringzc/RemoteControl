from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth


class getPhoneNumber(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return JsonResponse({
            'result': "success",
            'phoneNumber': request.user.phone_number,
        })
