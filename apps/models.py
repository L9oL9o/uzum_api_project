from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, \
    DecimalField, IntegerField, TextField, Model, EmailField, DateTimeField


class Catalog(Model):
    catalog = CharField(max_length=55)

    def __str__(self):
        return f"{self.catalog}"

    class Meta:
        db_table = 'Catalog'


class Category(Model):
    category = CharField(max_length=255)
    catalog = ForeignKey(Catalog, CASCADE)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        db_table = 'Category'


class Type(Model):
    type = CharField(max_length=255)
    category = ForeignKey(Category, CASCADE)

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = 'Type'


class User(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=55)
    password = CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'User'


class Products(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    desc = TextField(max_length=2500)
    short_desc = TextField(max_length=500)
    quantity = IntegerField(default=0)
    type = ForeignKey(Type, CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'Products'


class Seller(Model):
    name = CharField(max_length=255)
    nickname = CharField(max_length=55, unique=True)
    registered_at = DateTimeField(auto_now_add=True)
    products = ForeignKey(Products, CASCADE)

    def __str__(self):
        return f"{self.nickname}"

    class Meta:
        db_table = "Seller"


class Orders(Model):
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, CASCADE)
    seller = ForeignKey(Seller, CASCADE)
    product = ForeignKey(Products, CASCADE)
    quantity = IntegerField(default=1)
    price = DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.created_at}"

    class Meta:
        db_table = 'Orders'


class Discount(Model):
    name = CharField(max_length=255)
    product = ForeignKey(Products, CASCADE)
    discount = IntegerField(default=0)
    starts_at = DateTimeField(auto_now_add=True, blank=True)
    changed_at = DateTimeField(auto_now=True)
    ends_at = DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "Discount"
