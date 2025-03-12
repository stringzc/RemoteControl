from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models.User.User import User
from django.utils import timezone


class TokenAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').split('Bearer ')[-1]
        if not token:
            return None

        try:
            user = User.objects.get(token=token)
            if timezone.now() > user.token_expire:
                raise AuthenticationFailed('Token已过期')

            # 自动续期：距离过期不足1天时刷新
            if (user.token_expire - timezone.now()).days < 1:
                user.refresh_token()

            return user, None
        except User.DoesNotExist:
            raise AuthenticationFailed('无效Token')