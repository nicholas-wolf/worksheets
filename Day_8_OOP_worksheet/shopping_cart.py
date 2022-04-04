# As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list).
# As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.
# As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)
# As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.
from product import Product

class Shopping_Cart():
    def __init__(self):
        self.products = []

    def add_product(self):
        product_name = input("Add product name: ")
        product_price = input("Add product price: ")
        product_category = input("Add product category: ")
        new_product = Product(product_name, product_price, product_category)
        self.products.append(new_product)

    def add_total_of_cart(self):
        total = 0
        for product in self.products:
            total = total + product.price

        print("Total number of product's ", total)
    
    def empty_shopping_cart(self):
        self.products = []



