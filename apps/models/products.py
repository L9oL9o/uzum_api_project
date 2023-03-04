from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, TextField, Model, FloatField

from apps.models.categories import Type
from apps.models.seller import Seller


class Products(Model):
    name = CharField(max_length=255)
    price = FloatField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(100000000.00)
    ])
    desc = TextField(max_length=2500)
    short_desc = TextField(max_length=500)
    quantity = IntegerField(default=0)
    type = ForeignKey(Type, CASCADE)
    seller = ForeignKey(Seller, CASCADE)

    def __str__(self):
        return f"{self.name}"


class Meta:
    db_table = 'Products'
    verbose_name = 'Product'
    verbose_name_plural = 'Products'
