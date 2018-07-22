# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Exchange(models.Model):
    From = models.CharField(max_length=3)
    To = models.CharField(max_length=3)
    Date = models.DateField(auto_now_add=False)
    Rate = models.FloatField()


    class Meta:
        verbose_name = "Exchange"
        verbose_name_plural = "Exchanges"

    def __unicode__(self):
        return self.name
