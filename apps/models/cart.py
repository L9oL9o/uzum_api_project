from django.db.models import ForeignKey, Model, ManyToManyField, DO_NOTHING
from django.contrib.auth import get_user_model

from apps.models.products import Products

User = get_user_model()


class Cart(Model):
    customer = ForeignKey(User, related_name='user', on_delete=DO_NOTHING)
    products = ManyToManyField(Products, blank=True, related_name='products')
