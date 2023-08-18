# BankingSystem in Python, which models a simple banking system 
# with accounts, transactions, and customer management:
class Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Encapsulated attribute
        self._balance = balance  # Encapsulated attribute
        self._transactions = []  # Encapsulated attribute for transaction history

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Deposited ${amount:.2f}")
            print(f"Deposited ${amount:.2f} into Account {self._account_number}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrew ${amount:.2f}")
            print(f"Withdrew ${amount:.2f} from Account {self._account_number}")
        else:
            print(f"Insufficient balance in Account {self._account_number}")

    def get_balance(self):
        return self._balance

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self._transactions:
            print(transaction)


class Customer:
    def __init__(self, name, customer_id):
        self._name = name  # Encapsulated attribute
        self._customer_id = customer_id  # Encapsulated attribute
        self._accounts = {}  # Encapsulated attribute for customer's accounts

    def create_account(self, account_number, initial_balance):
        if account_number not in self._accounts:
            self._accounts[account_number] = Account(account_number, initial_balance)
            print(f"Account {account_number} created for {self._name}")

    def get_account(self, account_number):
        return self._accounts.get(account_number)

    def display_info(self):
        print(f"Customer: {self._name}")
        print(f"Customer ID: {self._customer_id}")
        print("Accounts:")
        for account_number, account in self._accounts.items():
            print(f"Account {account_number}: Balance - ${account.get_balance():.2f}")


class BankingSystem:
    def __init__(self):
        self._customers = {}  # Encapsulated attribute for bank's customers

    def add_customer(self, customer):
        self._customers[customer._customer_id] = customer
        print(f"Added {customer._name} to the banking system")

    def get_customer(self, customer_id):
        return self._customers.get(customer_id)

    def display_customers(self):
        print("Bank Customers:")
        for customer_id, customer in self._customers.items():
            print(f"Customer ID: {customer_id} - Name: {customer._name}")


# Creating instances of the Account, Customer, and BankingSystem classes
customer1 = Customer("Alice Johnson", "C123")
customer2 = Customer("Bob Smith", "C456")

account1 = Account("A12345", 1000)
account2 = Account("A67890", 500)

bank = BankingSystem()

# Using encapsulated methods to interact with the objects
customer1.create_account("A11111", 2000)
customer1.create_account("A22222", 1500)
customer2.create_account("A33333", 800)

bank.add_customer(customer1)
bank.add_customer(customer2)

customer1.get_account("A11111").deposit(300)
customer1.get_account("A11111").withdraw(150)
customer1.get_account("A22222").deposit(500)
customer2.get_account("A33333").withdraw(200)

customer1.display_info()
customer2.display_info()

bank.display_customers()

customer1.get_account("A11111").display_transactions()
