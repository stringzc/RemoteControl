from django.db import models

from Monitor.models.Mode.Mode import Mode
from Monitor.models.Plan.Plan import Plan


class PlanMode(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('plan', 'mode')  # 确保每个方案与模式的组合唯一
