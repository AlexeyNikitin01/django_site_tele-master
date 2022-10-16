from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import RepairOrderViewSet, TVSaleViewSet, OrderViewSet


router = DefaultRouter()
router.register('repair_order', RepairOrderViewSet)
router.register('tv_sale', TVSaleViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
