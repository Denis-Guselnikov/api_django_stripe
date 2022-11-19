from django.urls import include, path
from .views import ItemViewSet
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()

v1_router.register('buy', ItemViewSet, basename='buy_item')
v1_router.register('item', ItemViewSet, basename='items')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
