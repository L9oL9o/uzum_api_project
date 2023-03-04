from django.db.models import CharField, ForeignKey, CASCADE, DecimalField, IntegerField, Model, DateTimeField, TextChoices

from apps.models.customer import Customer
from apps.models.products import Products
from apps.models.seller import Seller


class Orders(Model):
    class StatusChoice(TextChoices):
        ORDERED = 'ordered'
        DELIVERING = 'delivering'
        DELIVERED = 'delivered'

    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(Customer, CASCADE)
    seller = ForeignKey(Seller, CASCADE)
    product = ForeignKey(Products, CASCADE)
    status = CharField(max_length=55, choices=StatusChoice.choices, default=StatusChoice.ORDERED)
    quantity = IntegerField(default=1)
    price = DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.created_at}"

    class Meta:
        db_table = 'Orders'
