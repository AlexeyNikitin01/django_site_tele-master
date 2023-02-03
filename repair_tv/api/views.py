from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import pagination, permissions, generics
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import get_object_or_404

from .serializers import RepairOrderSerializer, TVSaleSerializer, \
    OrderSerializer, UserSerializer, UserProfileSerializer, RegisterSerializer, CommentSerializer

from main.models import RepairOrder, TVSale
from main.forms import RepairOrderForm
from orders.models import Order
from tm_user.models import ProfileUser
from comment.models import Comment


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
        send_mail(f'От {form.cleaned_data["name"]} | {form.cleaned_data["phone"]}',
                  form.cleaned_data["description"], 'lyosha-2001@mail.ru', ['lyosha-2001@mail.ru'])
        repair_order.save()

        return Response({'repair_order_id': repair_order.id})


class TVSalePaginator(pagination.PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'


class TVSaleViewSet(ModelViewSet):
    search_fields = ['$model_tv', '$description_tv']
    filter_backends = (filters.SearchFilter,)
    queryset = TVSale.objects.all()
    serializer_class = TVSaleSerializer
    pagination_class = TVSalePaginator
    permission_classes = [permissions.AllowAny]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserProfileViewSet(ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        return Response({'username': user.username})


class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args,  **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Пользователь успешно создан",
        })


class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if self.kwargs:
            pk_tv = self.kwargs['pk']
            tv = TVSale.objects.get(pk=pk_tv)
            return Comment.objects.filter(com_to_model=tv)
        return Comment.objects.all()
