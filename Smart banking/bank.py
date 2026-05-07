
from account import Account
import data_handler as dh


class Bank:

    def create_account(self):
        name = input("Enter Name: ")
        acc_no = int(input("Enter Account Number: "))
        pin = int(input("Set PIN: "))
        balance = float(input("Initial Deposit: "))

        acc = Account(name, acc_no, pin, balance)
        dh.save_account(acc)
        print("Account Created Successfully!")

    def login(self):
        acc_no = int(input("Enter Account Number: "))
        pin = int(input("Enter PIN: "))

        user = dh.authenticate(acc_no, pin)

        if user is None:
            print("Invalid Credentials")
            return

        acc = Account(user["Name"], user["AccNo"], user["Pin"], user["Balance"])
        self.user_menu(acc)

    def user_menu(self, acc):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Logout")
            choice = input("Choose: ")
            if choice == "1":
                amount = float(input("Enter amount: "))
                acc.deposit(amount)
                dh.update_account(acc)

            elif choice == "2":
                amount = float(input("Enter amount: "))
                acc.withdraw(amount)
                dh.update_account(acc)

            elif choice == "3":
                acc.display_balance()

            elif choice == "4":
                print("Logged out")
                break