from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from Monitor.authentication import TokenAuth


class UserProfileView(APIView):
    authentication_classes = [TokenAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.refresh_time():
            return Response({
                "openid": user.openid,
                "last_login": user.last_login
            })
        else:
            return Response({"error": "Token expired"}, status=401)
