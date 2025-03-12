from django.db import models


class Device(models.Model):
    Device_id = models.CharField(max_length=255, primary_key=True)  # 设备ID，字符串类型
    name = models.CharField(max_length=255)  # 设备名称
    active = models.IntegerField(default=0)  # 默认值为0

    def __str__(self):
        return self.name
