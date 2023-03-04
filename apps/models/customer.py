from django.db.models import CharField, Model, EmailField


class Customer(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=55)
    password = CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'User'
