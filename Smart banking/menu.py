# menu.py

from account_manager import AccountManager
from transaction_manager import TransactionManager

def start_menu():
    acc_manager = AccountManager()
    trans_manager = TransactionManager()

    while True:
        print("\n--- SMART BANKING SYSTEM ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc_no = input("Account Number: ")
            name = input("Holder Name: ")
            pin = input("PIN: ")
            deposit = float(input("Initial Deposit: "))
            acc_manager.create_account(acc_no, name, pin, deposit)

        elif choice == "2":
            acc_no = input("Account Number: ")
            pin = input("PIN: ")
            account = acc_manager.get_account(acc_no, pin)

            if account:
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Logout")
                    ch = input("Choice: ")

                    if ch == "1":
                        amt = float(input("Amount: "))
                        trans_manager.make_deposit(account, amt)

                    elif ch == "2":
                        amt = float(input("Amount: "))
                        trans_manager.make_withdraw(account, amt)

                    elif ch == "3":
                        print("Current Balance:", account.view_balance())

                    elif ch == "4":
                        break
            else:
                print("Invalid login!")

        elif choice == "3":
            break