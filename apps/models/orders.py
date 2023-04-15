from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, Model, DateTimeField, \
    TextChoices, ManyToManyField, DecimalField, PositiveIntegerField, EmailField, BooleanField

from apps.models import Product


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


# ~~~ chat gpt

class Order(Model):
    user = ForeignKey(User, related_name='orders', on_delete=CASCADE)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField()
    address = CharField(max_length=250)
    created = DateTimeField(auto_now_add=True)
    paid = BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(Model):
    order = ForeignKey(Order, related_name='items', on_delete=CASCADE)
    product = ForeignKey(Product, related_name='order_items', on_delete=CASCADE)
    price = DecimalField(max_digits=10, decimal_places=2)
    quantity = PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
