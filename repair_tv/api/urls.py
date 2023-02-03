from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import RepairOrderViewSet, TVSaleViewSet, OrderViewSet,\
    UserViewSet, UserProfileViewSet, RegisterView, ProfileView, CommentView


router = DefaultRouter()
router.register('repair_order', RepairOrderViewSet)
router.register('tv_sale', TVSaleViewSet)
router.register('order', OrderViewSet)
router.register('user', UserViewSet)
router.register('user_profile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('comment/', CommentView.as_view()),
    path('comment/<int:pk>/', CommentView.as_view()),
]
