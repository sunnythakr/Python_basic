# a E-commerceSystem in Python, which models an online e-commerce 
# platform with products, shopping carts, and orders:

class Product:
    def __init__(self, product_id, name, price):
        self._product_id = product_id  # Encapsulated attribute
        self._name = name  # Encapsulated attribute
        self._price = price  # Encapsulated attribute

    def display_info(self):
        print(f"Product ID: {self._product_id}")
        print(f"Product Name: {self._name}")
        print(f"Price: ${self._price:.2f}")


class ShoppingCart:
    def __init__(self):
        self._items = {}  # Encapsulated attribute for cart items

    def add_item(self, product, quantity):
        if product._product_id in self._items:
            self._items[product._product_id] += quantity
        else:
            self._items[product._product_id] = quantity
        print(f"Added {quantity} {product._name}(s) to the cart")

    def remove_item(self, product, quantity):
        if product._product_id in self._items:
            self._items[product._product_id] -= quantity
            if self._items[product._product_id] <= 0:
                del self._items[product._product_id]
            print(f"Removed {quantity} {product._name}(s) from the cart")
        else:
            print(f"{product._name} not found in the cart")

    def calculate_total(self, products):
        total = sum([products[product_id]._price * quantity for product_id, quantity in self._items.items()])
        return total

    def display_cart(self, products):
        if self._items:
            print("Shopping Cart:")
            for product_id, quantity in self._items.items():
                product = products[product_id]
                print(f"{product._name} - Quantity: {quantity}")
            total = self.calculate_total(products)
            print(f"Total: ${total:.2f}")
        else:
            print("Shopping Cart is empty")


class Order:
    _order_counter = 0

    def __init__(self, cart, total):
        Order._order_counter += 1
        self._order_id = Order._order_counter
        self._cart = cart  # Encapsulated attribute
        self._total = total  # Encapsulated attribute

    def display_info(self, products):
        print(f"Order ID: {self._order_id}")
        self._cart.display_cart(products)
        print(f"Total: ${self._total:.2f}")


class EcommerceSystem:
    def __init__(self):
        self._products = {}  # Encapsulated attribute for products

    def add_product(self, product):
        self._products[product._product_id] = product
        print(f"Added '{product._name}' to the product list")

    def display_products(self):
        print("Available Products:")
        for product in self._products.values():
            product.display_info()

    def create_order(self, cart):
        total = cart.calculate_total(self._products)
        order = Order(cart, total)
        return order


# Creating instances of the Product, ShoppingCart, Order, and EcommerceSystem classes
product1 = Product("P123", "Laptop", 1000)
product2 = Product("P456", "Headphones", 50)
product3 = Product("P789", "Mouse", 15)

ecommerce = EcommerceSystem()

ecommerce.add_product(product1)
ecommerce.add_product(product2)
ecommerce.add_product(product3)

shopping_cart = ShoppingCart()
shopping_cart.add_item(product1, 2)
shopping_cart.add_item(product2, 3)
shopping_cart.add_item(product3, 1)
shopping_cart.display_cart(ecommerce._products)

shopping_cart.remove_item(product2, 1)
shopping_cart.display_cart(ecommerce._products)

order = ecommerce.create_order(shopping_cart)
order.display_info(ecommerce._products)
