from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import RepairOrderSerializer, TVSaleSerializer, OrderSerializer

from main.models import RepairOrder, TVSale
from main.forms import RepairOrderForm
from orders.models import Order


class RepairOrderViewSet(ModelViewSet):
    queryset = RepairOrder.objects.all()
    serializer_class = RepairOrderSerializer

    def create(self, request):
        form = RepairOrderForm(request.POST)
        if not form.is_valid():
            return Response({'errors': form.errors}, status=400)
        repair_order = RepairOrder.objects.create(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            phone=form.cleaned_data['phone'],
            description=form.cleaned_data['description'],
        )
        repair_order.save()

        return Response({'repair_order_id': repair_order.id})


class TVSaleViewSet(ModelViewSet):
    queryset = TVSale.objects.all()
    serializer_class = TVSaleSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
