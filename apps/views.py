from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.models import Seller, User, Orders, Category, Discount, Products, Type, Catalog
from apps.serializers import SellerModelSerializer, UserModelSerializer, OrdersModelSerializer, CategoryModelSerializer, \
    DiscountModelSerializer, ProductsModelSerializer, TypeModelSerializer, CatalogModelSerializer


class OrderModelViewSet(ModelViewSet):
    serializer_class = OrdersModelSerializer
    queryset = Orders.objects.order_by('-created_at')


class SellerModelViewSet(ModelViewSet):
    serializer_class = SellerModelSerializer
    queryset = Seller.objects.order_by('-created_at')


class CatalogModelViewSet(ModelViewSet):
    serializer_class = CatalogModelSerializer
    queryset = Catalog.objects.all()


class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()


class TypeModelViewSet(ModelViewSet):
    serializer_class = TypeModelSerializer
    queryset = Type.objects.all()


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductsModelSerializer
    queryset = Products.objects.all()


class DiscountModelViewSet(ModelViewSet):
    serializer_class = DiscountModelSerializer
    queryset = Discount.objects.all('-created_at')


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.order_by('-created-at')
