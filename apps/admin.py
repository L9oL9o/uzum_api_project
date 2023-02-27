from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Products, Category, Seller, Catalog, Discount, Orders, User, Type


class CatalogAdmin(ModelAdmin):
    list_display = ('catalog',)


class CategoryAdmin(ModelAdmin):
    list_display = ['category']


class TypeAdmin(ModelAdmin):
    list_display = ['type']


class UserAdmin(ModelAdmin):
    list_display = ['name', 'email']


class ProductsAdmin(ModelAdmin):
    list_display = ('name', 'price', 'type', 'seller', 'quantity',)


class SellerAdmin(ModelAdmin):
    list_display = ['name', 'nickname']


class OrdersAdmin(ModelAdmin):
    list_display = ['created_at', 'user', 'seller', 'product', 'quantity']


class DiscountAdmin(ModelAdmin):
    list_display = ['name', 'discount', 'product', 'starts_at', 'ends_at']


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Discount, DiscountAdmin)
