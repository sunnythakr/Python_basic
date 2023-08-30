class PaymentMethod:
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number, expiration_date):
        self.card_number = card_number
        self.expiration_date = expiration_date
    
    def process_payment(self, amount):
        print(f"Processing ${amount} payment using credit card {self.card_number}...")

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        print(f"Processing ${amount} payment using PayPal account {self.email}...")

class Cryptocurrency(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def process_payment(self, amount):
        print(f"Processing ${amount} payment using cryptocurrency wallet {self.wallet_address}...")

# Create instances of different payment methods
credit_card = CreditCard("1234-5678-9012-3456", "12/25")
paypal = PayPal("user@example.com")
cryptocurrency = Crypt
