from django.db.models import CharField, Model, DateTimeField


class Seller(Model):
    name = CharField(max_length=255)
    nickname = CharField(max_length=55, unique=True)
    registered_at = DateTimeField(auto_now_add=True)

    # products = ForeignKey(Products, CASCADE)

    def __str__(self):
        return f"{self.nickname}"

    class Meta:
        db_table = "Seller"
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
