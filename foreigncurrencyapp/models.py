# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CurrenciesFrom(models.Model):
    currency_name = models.CharField(max_length=3)

    def __str__(self):
        return self.currency_name

class CurrenciesTo(models.Model):
    currency_name = models.CharField(max_length=3)

    def __str__(self):
        return self.currency_name

class Exchange(models.Model):
    from_currency = models.ForeignKey(CurrenciesFrom, on_delete=models.CASCADE)
    to_currency = models.ForeignKey(CurrenciesTo, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s %s %s' % (self.from_currency, '>', self.to_currency)


class DailyRate(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    rate = models.FloatField()
    date = models.DateField(auto_now_add=False)
