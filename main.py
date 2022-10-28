__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *


def main():
    pass
    # print(search('Cap'))
    # list_user_products(1)
    # print(list_products_per_tag(4))
    # add_product_to_catalog(1, 'shampoo bar')
    # remove_product(1, 4)
    # list_user_products(1)
    # update_stock(1, 4)
    # purchase_product(1, 2, 2)


def search(term):
    return [product.name for product in Product.select().where(
        (Product.name.contains(term)) | (Product.description.contains(term)))]


def list_user_products(user_id):
    product_list = [product.name for product in Product.select().join(
        UserProduct).join(User).where(User.id == user_id)]
    user_name = User.get(User.id == user_id).name

    print('{} sells {}'.format(user_name, product_list))


def list_products_per_tag(tag_id):
    return [tag.product.name for tag in Tag.select(Tag, Product).join(Product).where(Tag.id == tag_id)]


def add_product_to_catalog(user_id, product):
    user = User.get(User.id == user_id)
    user.products_owned.add(Product.get(Product.name == product))
    print('Added {} to {}'.format(product, user.name))


def update_stock(product_id, new_quantity):
    product_name = Product.get(Product.id == product_id).name
    (Product
     .update(quantity=new_quantity)
     .where(Product.id == product_id)
     .execute())
    print("{}'s new stock: {}".format(product_name, new_quantity))


def purchase_product(product_id, buyer_id, quantity):
    amount = (Product.get(Product.id == product_id).quantity) - (quantity)
    product = Product.get(Product.id == product_id)
    buyer = User.get(User.id == buyer_id)
    (Transaction
     .create(user_id=buyer,
             product_id=product,
             quantity=quantity))
    (Product
     .update(quantity=amount)
     .where(Product.id == product_id)
     .execute())
    print('{} bought {} {}'.format(buyer.name, quantity, product.name))


def remove_product(user_id, product_id):
    user = User.get(User.id == user_id)
    product_name = Product.get(Product.id == product_id).name
    user.products_owned.remove(
        Product.get(Product.id == product_id))
    print('Removed {} from {}'.format(product_name, user.name))


if __name__ == "__main__":
    main()
