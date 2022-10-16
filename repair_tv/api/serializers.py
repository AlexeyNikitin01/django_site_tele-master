from rest_framework.serializers import ModelSerializer

from main.models import RepairOrder, TVSale


class RepairOrderSerializer(ModelSerializer):
    class Meta:
        model = RepairOrder
        fields = '__all__'


class TVSaleSerializer(ModelSerializer):
    class Meta:
        model = TVSale
        fields = '__all__'
