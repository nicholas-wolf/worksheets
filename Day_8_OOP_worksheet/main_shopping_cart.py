# As a developer, I want to import the Customer and Product classes into main.py so I can instantiate a customer object as well as three Product objects and interact with the object’s methods:
# 1. Print the customer’s name to the terminal
# 2. Call the customer’s add product to shopping cart method three times and add the three products objects you created
# 3. Call the customer’s view products method
# 4. Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal
# 5. Call the customer’s shopping cart’s empty cart method
# 6. Check if all products have been removed from the shopping car


from customer import Customer


customer = Customer("Bob")

print(customer.name)

customer.add_customer_product()
customer.add_customer_product()
customer.add_customer_product()
customer.all_products()
customer.customer_cart.add_total_of_cart()
customer.customer_cart.empty_shopping_cart()
customer.all_products()
