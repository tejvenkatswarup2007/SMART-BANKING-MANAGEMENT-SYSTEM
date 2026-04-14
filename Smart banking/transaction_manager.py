# transaction_manager.py

from transaction import Transaction

class TransactionManager:
    def make_deposit(self, account, amount):
        account.deposit(amount)
        t = Transaction(account.account_number, "Deposit", amount)
        account.transactions.append(t)
        print("Deposit successful!")

    def make_withdraw(self, account, amount):
        if account.withdraw(amount):
            t = Transaction(account.account_number, "Withdraw", amount)
            account.transactions.append(t)
            print("Withdraw successful!")
        else:
            print("Insufficient balance!")