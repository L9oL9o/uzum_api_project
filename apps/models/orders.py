from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, Model, DateTimeField, \
    TextChoices, ManyToManyField

from apps.models.customer import Customer
from apps.models.products import Products
from apps.models.seller import Seller


class Orders(Model):
    class StatusChoice(TextChoices):
        ORDERED = 'ordered'
        DELIVERING = 'delivering'
        DELIVERED = 'delivered'

    created_at = DateTimeField(auto_now_add=True)
    customer = ForeignKey(Customer, CASCADE)
    seller = ManyToManyField(Seller)
    product = ManyToManyField(Products)
    status = CharField(max_length=55, choices=StatusChoice.choices, default=StatusChoice.ORDERED)
    quantity = IntegerField(default=1)

    def __str__(self):
        return f"{self.created_at}"

    class Meta:
        db_table = 'Orders'
