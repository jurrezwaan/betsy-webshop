# Models go here
import peewee

db = peewee.SqliteDatabase("database.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = peewee.CharField()
    description = peewee.TextField()
    price = peewee.FloatField()
    quantity = peewee.IntegerField()


class User(BaseModel):
    name = peewee.CharField()
    address = peewee.TextField()
    billing_info = peewee.TextField()
    products_owned = peewee.ManyToManyField(Product)


class Transaction():
    user_id = peewee.ForeignKeyField(User)
    product_id = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()
