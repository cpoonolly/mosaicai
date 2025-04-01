from tortoise.models import Model
from tortoise import fields


class Book(Model):
    id = fields.IntField(primary_key=True)
    title = fields.CharField(max_length=100)
    author = fields.CharField(max_length=100)
    ISBN = fields.CharField(unique=True, max_length=13)
    publication_time = fields.DatetimeField()
    genre = fields.CharField(max_length=50)
    price = fields.DecimalField(decimal_places=2, max_digits=10)
    quantity = fields.IntField()