# account.py

class Account:
    def __init__(self, account_number, holder_name, pin, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def view_balance(self):
        return self.balance