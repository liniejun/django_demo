# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=30)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=10,decimal_places=2)
    gunit = models.CharField(max_length=20)
    gclick = models.IntegerField() # 点击量，作为人气
    gdesc = models.CharField(max_length=500)
    gcontent = HTMLField() #  富文本编辑器
    ginventory = models.IntegerField()
    gtype = models.ForeignKey(TypeInfo)
    gadv = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gtitle.encode('utf-8')


