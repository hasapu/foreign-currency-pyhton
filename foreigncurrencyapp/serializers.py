from rest_framework import serializers
from .models import CurrenciesFrom, CurrenciesTo, Exchange, DailyRate

class CurrencyFromSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrenciesFrom
        fields = ('id', 'currency_name')

class CurrencyToSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrenciesTo
        fields = ('id', 'currency_name')

class ExchangeSerializer(serializers.ModelSerializer):
    # from_currency = serializers.StringRelatedField()
    # to_currency = serializers.StringRelatedField()
    class Meta:
        model = Exchange
        fields = ('id', 'from_currency', 'to_currency')

class DailyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRate
        fields = ('id', 'exchange', 'rate', 'date')
