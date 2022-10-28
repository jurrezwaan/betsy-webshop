__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *


def main():
    # print(search('glockenspiel'))
    # list_user_products(1)
    # print(list_products_per_tag(4))
    # # add_product_to_catalog(1, 'shampoo bar')
    # update_stock(1, 4)
    purchase_product(1, 2, 1)


def search(term):
    return [product for product in Product.select().where(Product.name.contains(term))]


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


def update_stock(product_id, new_quantity):
    product_name = Product.get(product_id == product_id).name
    (Product
     .update(quantity=new_quantity)
     .where(Product.id == product_id)
     .execute())
    print('{}''s new stock : {}'.format(product_name, new_quantity))

# lukt niet om row toe te voegen aan Transaction. Hij herkent de fields niet. Niet met create ook niet met insert


def purchase_product(product_id, buyer_id, quantity):
    product = Product.get(Product.id == product_id)
    buyer = User.get(User.id == buyer_id)
    Transaction.create(user_id == buyer, product_id ==
                       product, quantity == quantity)


def remove_product(user_id, product_id):
    user = User.get(User.id == user_id)
    user.products_owned.remove(
        Product.select().where(Product.id == product_id))


if __name__ == "__main__":
    main()
