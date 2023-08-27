# EcommerceStore simulation in Python. This example models an online store 
# with products, customers, shopping carts, orders, and payments. It
#  showcases encapsulation, interactions, and system management 
class Product:
    def __init__(self, product_id, name, price):
        self._product_id = product_id
        self._name = name
        self._price = price

    def display_info(self):
        print(f"Product ID: {self._product_id}")
        print(f"Name: {self._name}")
        print(f"Price: ${self._price:.2f}")


class Customer:
    def __init__(self, customer_id, name, email):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._shopping_cart = []

    def add_to_cart(self, product):
        self._shopping_cart.append(product)
        print(f"Added '{product._name}' to {self._name}'s cart")

    def remove_from_cart(self, product):
        if product in self._shopping_cart:
            self._shopping_cart.remove(product)
            print(f"Removed '{product._name}' from {self._name}'s cart")
        else:
            print(f"'{product._name}' is not in {self._name}'s cart")
  
    def display_info(self):
        print(f"Customer ID: {self._customer_id}")
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")

    def display_cart(self):
        print("Shopping Cart:")
        for product in self._shopping_cart:
            print(f"Product: '{product._name}' - Price: ${product._price:.2f}")


class Order:
    def __init__(self, order_id, customer, products):
        self._order_id = order_id
        self._customer = customer
        self._products = products

    def calculate_total(self):
        total = sum(product._price for product in self._products)
        return total

    def display_info(self):
        print(f"Order ID: {self._order_id}")
        print(f"Customer: {self._customer._name}")
        print("Products:")
        for product in self._products:
            print(f"'{product._name}' - Price: ${product._price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


class EcommerceStore:
    def __init__(self):
        self._products = {}
        self._customers = {}
        self._orders = []
        self._order_counter = 1

    def add_product(self, product):
        self._products[product._product_id] = product
        print(f"Added product '{product._name}' to the store")

    def add_customer(self, customer):
        self._customers[customer._customer_id] = customer
        print(f"Added customer {customer._name} to the store")

    def create_order(self, customer_id, product_ids):
        customer = self._customers.get(customer_id)
        if customer:
            products = [self._products.get(product_id) for product_id in product_ids]
            products = [product for product in products if product is not None]
            if products:
                order = Order(self._order_counter, customer, products)
                self._orders.append(order)
                self._order_counter += 1
                print(f"Order created for {customer._name}")
            else:
                print("Invalid product IDs")
        else:
            print("Invalid customer ID")

    def display_orders(self):
        print("Orders:")
        for order in self._orders:
            order.display_info()


# Creating instances of the Product, Customer, and EcommerceStore classes
store = EcommerceStore()

product1 = Product("P001", "Laptop", 999.99)
product2 = Product("P002", "Headphones", 49.99)
product3 = Product("P003", "Keyboard", 29.99)

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

customer1 = Customer("C001", "Alice Johnson", "alice@example.com")
customer2 = Customer("C002", "Bob Smith", "bob@example.com")

store.add_customer(customer1)
store.add_customer(customer2)

customer1.add_to_cart(product1)
customer1.add_to_cart(product2)
customer2.add_to_cart(product3)

customer1.remove_from_cart(product2)

customer1.display_cart()

store.create_order("C001", ["P001", "P003"])
store.create_order("C002", ["P002"])

store.display_orders()
