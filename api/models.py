from django.db import models

# Create your models here.


from django.db import models


class User(models.Model):
    """用户表"""
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=64, verbose_name="密码")
    token = models.CharField(max_length=64, verbose_name="TOKEN", null=True, blank=True)
