from rest_framework.serializers import ModelSerializer

from main.models import RepairOrder, TVSale
from orders.models import Order, OrderItem


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
