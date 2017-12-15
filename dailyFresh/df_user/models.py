from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    df_name = models.CharField(max_length=20)
    df_pwd = models.CharField(max_length=100)
    df_email = models.CharField(max_length=50)
    df_phone = models.CharField(max_length=20)
    df_addr = models.CharField(max_length=100, default='')
    df_sname = models.CharField(max_length=20, default='')
    df_emailCode = models.CharField(max_length=20, default='')
    isDelete = models.BooleanField(default=False)