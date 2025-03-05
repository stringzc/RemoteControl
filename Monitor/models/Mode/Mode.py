from django.db import models


class Mode(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # 模式ID，字符串类型
    name = models.CharField(max_length=255)  # 模式名称
    description = models.TextField()  # 模式描述
    url = models.URLField()  # 模式的URL链接

    def __str__(self):
        return self.name
