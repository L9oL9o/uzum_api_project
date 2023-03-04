from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models.categories import Catalog, Category, Type
from apps.models.customer import Customer
from apps.models.discounts import Discount
from apps.models.orders import Orders
from apps.models.products import Products
from apps.models.seller import Seller


class CatalogAdmin(ModelAdmin):
    list_display = ('catalog',)


class CategoryAdmin(ModelAdmin):
    list_display = ['category', 'catalog']


class TypeAdmin(ModelAdmin):
    list_display = ['type', 'category']


class CustomerAdmin(ModelAdmin):
    list_display = ['name', 'email']


class ProductsAdmin(ModelAdmin):
    list_display = ('name', 'price', 'type', 'seller', 'quantity',)


class SellerAdmin(ModelAdmin):
    list_display = ['name', 'nickname']


class OrdersAdmin(ModelAdmin):
    list_display = ['created_at', 'status', 'user', 'seller', 'product', 'quantity']


class DiscountAdmin(ModelAdmin):
    list_display = ['name', 'discount', 'product', 'starts_at', 'ends_at']


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Discount, DiscountAdmin)
