from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Products, Category, Seller, Catalog, Discount, Orders, User, Type


class CatalogAdmin(ModelAdmin):
    list_display = ('catalog',)
