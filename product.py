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
    """
    Edit a current product in the products list

    Args:
        product_id: ID of the product to edit
    Returns:
        bool: True if product edited successfully, False otherwise
    """
    # Find the product to see if it exists
    for current_product in products:
        if current_product.id == product_id:
            #edit the product if the product exits
            current_product.name = input("Enter new product name: ")
            current_product.description = input("Enter new product description: ")
            current_product.price = float(input("Enter new product price: "))
            current_product.quantity = int(input("Enter new product quantity: "))
            return True
        else:
            return False  # Product ID not found, cannot edit

def delete_product(product_id):

def get_all_product(product_id):

def get_product_by_id(product):
