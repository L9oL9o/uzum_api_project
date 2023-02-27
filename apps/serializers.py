from rest_framework.serializers import ModelSerializer

from apps.models import Seller, Catalog, Category, Type, Products, User, Orders, Discount


class OrdersModelSerializer(ModelSerializer):
    class Meta:
        model = Orders
        exclude = ()
