# BankingSystem in Python, which models a bank with accounts,
#  transactions, and customer interactions:
class Account:
    def __init__(self, account_number, customer_name, initial_balance):
        self._account_number = account_number  # Encapsulated attribute
        self._customer_name = customer_name  # Encapsulated attribute
        self._balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount:.2f} into account {self._account_number}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self._account_number}")
        else:
            print("Invalid withdrawal amount")

    def display_balance(self):
        print(f"Account {self._account_number} balance: ${self._balance:.2f}")


class Transaction:
    def __init__(self, transaction_id, source_account, destination_account, amount):
        self._transaction_id = transaction_id  # Encapsulated attribute
        self._source_account = source_account  # Encapsulated attribute
        self._destination_account = destination_account  # Encapsulated attribute
        self._amount = amount  # Encapsulated attribute

    def process(self):
        if self._source_account._balance >= self._amount:
            self._source_account._balance -= self._amount
            self._destination_account._balance += self._amount
            print(f"Transaction {self._transaction_id} processed successfully")
        else:
            print(f"Insufficient balance for transaction {self._transaction_id}")


class BankingSystem:
    def __init__(self):
        self._accounts = {}  # Encapsulated attribute for accounts
        self._transactions = []  # Encapsulated attribute for transactions

    def create_account(self, account_number, customer_name, initial_balance):
        account = Account(account_number, customer_name, initial_balance)
        self._accounts[account_number] = account
        print(f"Created account {account_number} for {customer_name}")

    def get_account(self, account_number):
        return self._accounts.get(account_number)

    def perform_transaction(self, source_account, destination_account, amount):
        transaction_id = len(self._transactions) + 1
        transaction = Transaction(transaction_id, source_account, destination_account, amount)
        self._transactions.append(transaction)
        transaction.process()
    
    def display_accounts(self):
        print("Accounts:")
        for account in self._accounts.values():
            print(f"Account {account._account_number} - Customer: {account._customer_name}")


# Creating instances of the Account, Transaction, and BankingSystem classes
bank = BankingSystem()

bank.create_account("A101", "Alice Johnson", 1000)
bank.create_account("A102", "Bob Smith", 500)

alice_account = bank.get_account("A101")
bob_account = bank.get_account("A102")

alice_account.deposit(300)
bob_account.withdraw(200)

bank.perform_transaction(alice_account, bob_account, 400)

alice_account.display_balance()
bob_account.display_balance()

bank.display_accounts()
