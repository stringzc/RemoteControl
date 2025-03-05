from django.db import models


class Plan(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # 方案ID，字符串类型
    name = models.CharField(max_length=255)  # 方案名称
    phone_number = models.CharField(max_length=15)  # 方案绑定的手机号
    description = models.TextField()  # 方案描述

    def __str__(self):
        return self.name
