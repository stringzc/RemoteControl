from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)  # 用户的自增ID
    phone_number = models.CharField(max_length=15, unique=True)  # 用户手机号，确保唯一

    def __str__(self):
        return self.phone_number
