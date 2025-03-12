from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Monitor.authentication import TokenAuth
from Monitor.models.User.User import User


class savePhoneNumber(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone = request.data['phoneNumber']
        user = User.objects.get(openid=request.user.openid)
        if user:
            user.phone_number = phone
            user.save()
            return JsonResponse({
                'result': "success",
            })
        else:
            return JsonResponse({
                'result': "fail",
            })
