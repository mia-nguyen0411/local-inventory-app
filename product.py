# Define product class
from xmlrpc.client import boolean


class Product:
    def __init__(self, id, name, description, price, quantity):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

products = []

def add_product(product):
    """
    Add a new product to the products list

    Args:
        product: Product object to add
    Returns:
        bool: True if product added successfully, False otherwise
    """
    # check if product is in the list already
    for current_product in products:
        if current_product.id == product.id:
            return False  # Product ID already exists, cannot add
    
    # Add the product to the list
    result = boolean(products.append(product))
    if result:
        return True
    return False

def edit_product(product_id):

def delete_product(product_id):

def get_all_product(product_id):

def get_product_by_id(product):
