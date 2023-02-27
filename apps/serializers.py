from rest_framework.serializers import ModelSerializer

from apps.models import Seller, Catalog, Category, Type, Products, User, Orders, Discount


class OrdersModelSerializer(ModelSerializer):
    class Meta:
        model = Orders
        exclude = ()


class SellerModelSerializer(ModelSerializer):
    class Meta:
        model = Seller
        exclude = ()


class CatalogModelSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        exclude = ()


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class TypeModelSerializer(ModelSerializer):
    class Meta:
        model = Type
        exclude = ()


class ProductsModelSerializer(ModelSerializer):
    class Meta:
        model = Products
        exclude = ()


class DiscountModelSerializer(ModelSerializer):
    class Meta:
        model = Discount
        exclude = ()


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ()
