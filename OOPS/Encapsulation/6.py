class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Encapsulated attribute
        self._balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount} units")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount} units")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance

    def display_account_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Balance: {self._balance}")


# Creating instances of the BankAccount class
account1 = BankAccount("123456789", 1000)
account2 = BankAccount("987654321", 500)

# Using encapsulated methods to interact with the objects
account1.display_account_info()
account1.deposit(200)
account1.withdraw(300)
account1.display_account_info()

account2.display_account_info()
account2.deposit(1000)
account2.withdraw(800)
account2.display_account_info()
