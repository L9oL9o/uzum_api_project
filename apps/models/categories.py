from django.db.models import Model, CharField, ForeignKey, CASCADE


class Catalog(Model):
    catalog = CharField(max_length=55)

    def __str__(self):
        return f"{self.catalog}"

    class Meta:
        db_table = 'Catalog'


class Category(Model):
    category = CharField(max_length=255)
    catalog = ForeignKey(Catalog, CASCADE)

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
