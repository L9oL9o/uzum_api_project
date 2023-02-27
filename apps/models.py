from django.db import models
from django.db.models import Model, CharField


class Catalog(Model):
    catalog = CharField(max_length=55)

    def __str__(self):
        return f"{self.catalog}"

    class Meta:
        db_table = 'Catalog'
