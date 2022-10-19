__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *


def search(term):
    return Product.select().where(term.in_(Product.name))


def list_user_products(user_id):
    return User.select(User.products_owned).where(User.id == user_id)


def list_products_per_tag(tag_id):
    return (Product
            .select(Product, ProductTag, Tag)
            .join(ProductTag, on=(Product.id == ProductTag.product_id))
            .join(Tag, on=(ProductTag.tag_id == Tag.id)
                  .where(tag_id == Tag.id)))


def add_product_to_catalog(user_id, product):
    ...
    #  User.create()


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    product = Product.get(Product.id == product_id)
    product.delete_instance()
