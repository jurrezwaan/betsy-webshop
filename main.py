__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *


def search(term):
    return Product.select().where(Product.name.contains(term))


def list_user_products(user_id):
    product_list = [product.name for product in Product.select().join(
        UserProduct).join(User).where(User.id == user_id)]
    user_name = User.get(User.id == user_id).name

    print('{} sells {}'.format(user_name, product_list))


def list_products_per_tag(tag_id):
    return [product.name for product in Product.select().join(ProductTag).join(Tag).where(Tag.id == tag_id)]


def add_product_to_catalog(user_id, product):
    user = User.get(User.id == user_id)
    user.products_owned.add(Product.select().where(Product.name == product))


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(user_id, product_id):
    user = User.get(User.id == user_id)
    user.products_owned.remove(
        Product.select().where(Product.id == product_id))
