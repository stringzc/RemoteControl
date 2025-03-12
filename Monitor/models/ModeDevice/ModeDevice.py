from django.db import models

from Monitor.models.Device.Device import Device
from Monitor.models.Mode.Mode import Mode


class ModeDevice(models.Model):
    mode_id = models.ForeignKey(Mode, on_delete=models.CASCADE)
    Device_id = models.ForeignKey(Device, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('mode_id', 'Device_id')  # 确保每个模式与设备的组合唯一
