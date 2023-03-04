from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.models.cart import User
from apps.models.categories import Catalog, Category, Type
from apps.models.discounts import Discount
from apps.models.orders import Orders
from apps.models.products import Products
from apps.models.seller import Seller
from apps.serializers import SellerModelSerializer, UserModelSerializer, OrdersModelSerializer, CategoryModelSerializer, \
    DiscountModelSerializer, ProductsModelSerializer, TypeModelSerializer, CatalogModelSerializer


class OrderModelViewSet(ModelViewSet):
    serializer_class = OrdersModelSerializer
    queryset = Orders.objects.order_by()


class SellerModelViewSet(ModelViewSet):
    serializer_class = SellerModelSerializer
    queryset = Seller.objects.order_by()


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
    queryset = Discount.objects.all()


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.order_by()
