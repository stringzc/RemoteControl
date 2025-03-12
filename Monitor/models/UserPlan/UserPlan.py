from django.db import models

from Monitor.models.Plan.Plan import Plan
from Monitor.models.User.User import User


class UserPlan(models.Model):
    openid = models.CharField(max_length=128, unique=True)
    plan_id = models.CharField(max_length=128, unique=True)

    class Meta:
        unique_together = ('openid', 'plan_id')  # 确保每个用户与方案的组合唯一
