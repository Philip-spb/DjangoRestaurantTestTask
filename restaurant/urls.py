from rest_framework import routers
from django.urls import path
from django.conf.urls import include

from restaurant.views import FoodViewSet

router = routers.DefaultRouter()

app_name = 'api'

router.register(r'foods', FoodViewSet, 'foods')

urlpatterns = [
    path('', include(router.urls)),
]
