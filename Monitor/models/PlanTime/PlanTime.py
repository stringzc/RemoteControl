from django.db import models

from Monitor.models.Plan.Plan import Plan


class PlanTime(models.Model):
    Plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    StartTime = models.CharField(max_length=128, unique=True)
    EndTime = models.CharField(max_length=128, unique=True)

    class Meta:
        unique_together = ('Plan_id', 'StartTime', 'EndTime')  # 确保每个方案与模式的组合唯一
