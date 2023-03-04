from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, Model, DateTimeField

from apps.models.products import Products


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
