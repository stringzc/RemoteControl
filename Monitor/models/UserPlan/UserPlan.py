from django.db import models

from Monitor.models.Plan.Plan import Plan
from Monitor.models.User.User import User


class UserPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'plan')  # 确保每个用户与方案的组合唯一
