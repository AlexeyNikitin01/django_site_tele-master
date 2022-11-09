from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import RepairOrderViewSet, TVSaleViewSet, OrderViewSet, UserViewSet, UserProfileViewSet


router = DefaultRouter()
router.register('repair_order', RepairOrderViewSet)
router.register('tv_sale', TVSaleViewSet)
router.register('order', OrderViewSet)
router.register('user', UserViewSet)
router.register('user_profile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
