from django.contrib.auth import get_user_model
from django.db.models import Model, ForeignKey, CASCADE, ManyToManyField, DateTimeField, IntegerField, \
    DO_NOTHING, CharField

from apps.models import Product


class Discount(Model):
    name = CharField(max_length=255)
    product = ForeignKey(Product, CASCADE)
    discount = IntegerField(default=0)
    starts_at = DateTimeField(auto_now_add=True, blank=True)
    changed_at = DateTimeField(auto_now=True)
    ends_at = DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "Discount"


class Catalog(Model):
    catalog = CharField(max_length=55)

    def __str__(self):
        return f"{self.catalog}"

    class Meta:
        db_table = 'Catalog'


class Category(Model):
    category = CharField(max_length=255)
    catalog = ManyToManyField(Catalog)

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


User = get_user_model()
class Cart(Model):
    customer = ForeignKey(User, related_name='user', on_delete=DO_NOTHING)
    products = ManyToManyField(Product, blank=True, related_name='products')
