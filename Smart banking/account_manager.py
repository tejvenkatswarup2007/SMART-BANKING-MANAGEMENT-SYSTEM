# account_manager.py

from account import Account
from file_manager import save_account, load_accounts

class AccountManager:
    def __init__(self):
        self.accounts = load_accounts()

    def create_account(self, acc_no, name, pin, deposit):
        account = Account(acc_no, name, pin, deposit)
        save_account(account)
        self.accounts[acc_no] = [name, pin, deposit]
        print("Account created successfully!")

    def get_account(self, acc_no, pin):
        if acc_no in self.accounts and self.accounts[acc_no][1] == pin:
            name, _, balance = self.accounts[acc_no]
            return Account(acc_no, name, pin, balance)
        return None