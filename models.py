import peewee

db = peewee.SqliteDatabase("database.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = peewee.CharField(unique=True)
    description = peewee.TextField()
    price = peewee.DecimalField(decimal_places=2, auto_round=True)
    quantity = peewee.IntegerField(null=True)


class Tag(BaseModel):
    name = peewee.CharField(unique=True)
    product = peewee.ForeignKeyField(Product, backref='tags')


class User(BaseModel):
    name = peewee.CharField(unique=True)
    address = peewee.TextField()
    billing_info = peewee.TextField()
    products_owned = peewee.ManyToManyField(Product, backref='users')


class Transaction(BaseModel):
    user_id = peewee.ForeignKeyField(User, backref='transactions')
    product_id = peewee.ForeignKeyField(Product, backref='transactions')
    quantity = peewee.IntegerField()


UserProduct = User.products_owned.get_through_model()


def populate_test_data():
    db.create_tables([Product, Tag, User, Transaction, UserProduct])

    product_data = [
        ('glockenspiel', '''A glockenspiel is a metallophone,
        a musical instrument from the group of idiophones,
        consisting of two rows of metal bars (keys), usually without a resonator.''',
         10.50, 1, ('instrument', 'germany', 'metal')),
        ('necklace', '''Including velvet storage bag,
        a cleaning cloth and a care card with maintenance instructions.''',
         25, 1, ('jewellery', 'silver', 'french')),
        ('clogs', '''Clogs are a type of footwear made in part or completely from wood.
        Used worldwide, their forms can vary by culture,
        but often remained unchanged for centuries within a culture.''', 45, 1, ('shoes', 'wood', 'dutch')),
        ('shampoo bar', '''Enjoy a natural, intense purification of your hair and skin. For a truly pure and squeaky clean feeling.''',
         7.99, 1, ('shampoo', 'soap', 'vegan')),
        ('trucker cap', '''What is especially striking about the HFT RipStop Trucker Cap from Djinns is 
         the airy mesh insert at the back that provides excellent ventilation. 
         The snapback cap has press studs on the open back for an extra good fit. 
         The curved peak measures 7 cm and the crown 10.5 cm.''', 21.95, 1, ('cap', 'brown', 'trucker'))
    ]

    user_data = [
        ('claus', 'clausstrasse 1', 'DB10203040', ['glockenspiel']),
        ('emma', 'rue de emma 1', 'FB20103050', ['necklace']),
        ('bert', 'bertplantsoen 1', 'NB30501020', ['clogs'])
    ]

    for name, description, price, quantity, tags in product_data:
        product = Product.create(
            name=name, description=description, price=price, quantity=quantity)
        for tag in tags:
            Tag.create(name=tag, product=product)

    for name, address, billing_info, products_owned in user_data:
        user = User.create(
            name=name, address=address, billing_info=billing_info)
        for product in products_owned:
            user.products_owned.add(Product.get(Product.name == product))
