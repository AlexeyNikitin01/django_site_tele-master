from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer

from main.models import RepairOrder, TVSale
from orders.models import Order, OrderItem
from tm_user.models import ProfileUser


class RepairOrderSerializer(ModelSerializer):
    class Meta:
        model = RepairOrder
        fields = '__all__'


class TVSaleSerializer(ModelSerializer):
    class Meta:
        model = TVSale
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = '__all__'
