from django.db import models


class Device(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # 设备ID，字符串类型
    name = models.CharField(max_length=255)  # 设备名称

    def __str__(self):
        return self.name
