# from django.conf.urls import url
# from rest_framework import routers
# from foreigncurrencyapp.views import ExchangeViewSet
#
# router = routers.DefaultRouter()
# router.register(r'exchanges', ExchangeViewSet)



from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('currency-from', views.CurrencyFromViewSet)
router.register('currency-to', views.CurrencyToViewSet)
router.register('exchanges', views.ExchangeViewSet)
router.register('daily-rate', views.DailyRateViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
