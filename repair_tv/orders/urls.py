from django.urls import path

from .views import order_create_view
from .views import user_store_order_view

app_name = 'orders'
urlpatterns = [
    path('user_store_order/', user_store_order_view, name='user_store_order'),
    path('order_create/', order_create_view, name='order_create'),
]
