# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CurrenciesFrom, CurrenciesTo, Exchange, DailyRate

# Register your models here.
admin.site.register(CurrenciesFrom)
admin.site.register(CurrenciesTo)
admin.site.register(Exchange)
admin.site.register(DailyRate)
