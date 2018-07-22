# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import CurrenciesFrom, CurrenciesTo, Exchange, DailyRate
from .serializers import CurrencyFromSerializer, CurrencyToSerializer, ExchangeSerializer, DailyRateSerializer

# Create your views here.
class CurrencyFromViewSet(viewsets.ModelViewSet):
    queryset = CurrenciesFrom.objects.all()
    serializer_class = CurrencyFromSerializer

class CurrencyToViewSet(viewsets.ModelViewSet):
    queryset = CurrenciesTo.objects.all()
    serializer_class = CurrencyToSerializer

class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

class DailyRateViewSet(viewsets.ModelViewSet):
    queryset = DailyRate.objects.all()
    serializer_class = DailyRateSerializer
