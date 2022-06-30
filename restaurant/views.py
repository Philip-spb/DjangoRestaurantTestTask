from django.db.models import Count, Q
from rest_framework.viewsets import ReadOnlyModelViewSet

from restaurant.models import FoodCategory
from restaurant.serializers import FoodListSerializer


class FoodViewSet(ReadOnlyModelViewSet):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.annotate(cnt=Count('food', filter=Q(food__is_publish=True))).filter(cnt__gt=0)
