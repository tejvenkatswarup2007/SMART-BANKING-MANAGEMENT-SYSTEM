# file_manager.py

import csv

FILE_NAME = "accounts.csv"

def save_account(account):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([account.account_number, account.holder_name, account.pin, account.balance])

def load_accounts():
    accounts = {}
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                acc_no, name, pin, balance = row
                accounts[acc_no] = [name, pin, float(balance)]
    except FileNotFoundError:
        pass
    return accounts