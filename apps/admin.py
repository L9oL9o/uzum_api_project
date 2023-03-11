from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from apps.models.cart import Cart
from apps.models.categories import Catalog, Category, Type
from apps.models.customer import Customer
from apps.models.discounts import Discount
from apps.models.orders import Orders
from apps.models.products import Products
from apps.models.seller import Seller


class CatalogAdmin(ModelAdmin):
    list_display = ('catalog',)


class CategoryAdmin(ModelAdmin):
    list_display = ['category']


class TypeAdmin(ModelAdmin):
    list_display = ['type', 'category']


class CustomerAdmin(ModelAdmin):
    list_display = ['name', 'email']


class ProductsAdmin(ModelAdmin):
    list_display = ('name', 'price', 'type', 'seller', 'quantity',)


class SellerAdmin(ModelAdmin):
    list_display = ['name', 'nickname']


class OrdersAdmin(ModelAdmin):
    list_display = ('created_at', 'status', 'customer', 'quantity')  # <-- 'seller', 'product',


class DiscountAdmin(ModelAdmin):
    list_display = ['name', 'discount', 'product', 'starts_at', 'ends_at']


class CartAdmin(ModelAdmin):
    list_display = ['customer']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class CategoryInline(TabularInline):
#     model = Catalog
#     extra = 3
# class CategoryAddAdmin(ModelAdmin):
#     list_display = ['category']
#     inlines = [CategoryInline]
# admin.site.register(Category, CategoryAddAdmin)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Cart, CartAdmin)

#
# class MyForm(ModelForm):
#     class Meta:
#         model = Category
#
#     def __init__(self, *args, **kwargs):
#         super(MyForm, self).__init__(*args, **kwargs
#         self.fields['status'].widget = forms.RadioSelect(choices=self.fields['status'].choices)
#
#
# class AttendanceInline(admin.TabularInline):
#     model = Category
#     form = MyForm
#
#
# class EventAdmin(admin.ModelAdmin):
#     inlines = [AttendanceInline]
#
#     def save_model(self, request, obj, form, change):
#         obj.save()
#         for user in User.objects.all():
#             obj.attendance_set.create(user=user, status='')
#             # you should consider a null field or a possible choice for "Undecided"
#
#
# admin.site.register(Event, EventAdmin)
