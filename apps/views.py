from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.models import Seller, User, Orders, Category, Discount, Products, Type, Catalog
from apps.serializers import SellerModelSerializer, UserModelSerializer, OrdersModelSerializer, CategoryModelSerializer, \
    DiscountModelSerializer, ProductsModelSerializer, TypeModelSerializer, CatalogModelSerializer


class OrderModelViewSet(ModelViewSet):
    serializer_class = OrdersModelSerializer
    queryset = Orders.objects.order_by('-created_at')

