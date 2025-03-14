from django.db import models


class Plan(models.Model):
    planid = models.CharField(max_length=255, primary_key=True, unique=True)  # 方案ID，字符串类型
    name = models.CharField(max_length=255, null=True)  # 方案名称
    description = models.TextField(null=True)  # 方案描述
    updateTime = models.CharField(max_length=255, null=True)  # 更新时间
    active = models.IntegerField(default=0)  # 默认值为0
    icon = models.CharField(max_length=255, null=True)
    useTime = models.IntegerField(default=4)  # 默认值为0
    plan_device = models.CharField(max_length=255, null=True)  # 方案名称

    def __str__(self):
        return self.planid
