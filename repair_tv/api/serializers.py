from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer

from main.models import RepairOrder, TVSale
from orders.models import Order, OrderItem
from tm_user.models import ProfileUser
from comment.models import Comment


class RepairOrderSerializer(ModelSerializer):
    class Meta:
        model = RepairOrder
        fields = '__all__'


class TVSaleSerializer(ModelSerializer):
    class Meta:
        model = TVSale
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    user_order = serializers.CharField(source='user_order.username')

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


class RegisterSerializer(ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class CommentSerializer(ModelSerializer):
    com_to_model = serializers.CharField(source='com_to_model.slug_tv', read_only=False)
    id_model = serializers.IntegerField(source='com_to_model.pk', read_only=False)
    username = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        username = validated_data["username"]
        product = get_object_or_404(TVSale, pk=validated_data["com_to_model"]["pk"],
                                    slug_tv=validated_data["com_to_model"]["slug_tv"])
        comment = validated_data["comment"]
        pub_comment = Comment.objects.create(com_to_model=product, username=username, comment=comment)
        pub_comment.save()
        return pub_comment
