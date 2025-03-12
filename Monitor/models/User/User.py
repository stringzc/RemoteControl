from django.db import models
from django.utils import timezone
import secrets

from Aurage import settings


class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, null=True,  # 允许数据库存储 NULL
        blank=True)  # 用户手机号，确保唯一
    openid = models.CharField(max_length=128, unique=True)
    token = models.CharField(max_length=64, unique=True,  null=True)
    token_expire = models.DateTimeField(null=True)
    last_login = models.DateTimeField(auto_now=True,  null=True)  # 记录最后活跃时间
    @classmethod
    def generate_token(cls):
        return secrets.token_urlsafe(32)  # 生成高强度随机Token

    def refresh_token(self):
        self.token = self.generate_token()
        self.token_expire = timezone.now() + timezone.timedelta(days=settings.TOKEN_EXPIRE_DAYS)
        self.save()
        # 添加认证系统所需属性

    def refresh_time(self):
        now = timezone.now()
        # 检查是否存在token_expire且未过期
        if self.token_expire and now < self.token_expire:
            self.token_expire = now + timezone.timedelta(days=settings.TOKEN_EXPIRE_DAYS)
            self.save()  # auto_now=True会自动更新last_login
            return True
        else:
            return False

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False


