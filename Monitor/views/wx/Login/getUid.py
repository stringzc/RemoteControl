from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import requests
from Monitor.models.User.User import User
from django.utils import timezone


class getUid(APIView):
    def get(self, request):
        code = request.query_params.get('code')  # 从GET参数获取code

        if not code:
            return Response({"error": "Missing code"}, status=400)

        # 向微信服务器验证code
        wx_url = f"https://api.weixin.qq.com/sns/jscode2session?appid={settings.WX_APPID}&secret={settings.WX_SECRET}&js_code={code}&grant_type=authorization_code"
        wx_res = requests.get(wx_url).json()
        if 'errcode' in wx_res:
            return Response({"error": "微信登录失败"}, status=401)

        openid = wx_res['openid']
        # 获取或创建用户
        user, created = User.objects.get_or_create(openid=openid)
        if created or (timezone.now() > user.token_expire):
            user.refresh_token()
        if user.phone_number:
            return Response({
                "statues": True,
                "token": user.token,
                "expire": user.token_expire.timestamp()
            })
        else:
            return Response({
                "statues": False,
                "token": user.token,
                "expire": user.token_expire.timestamp()
            })