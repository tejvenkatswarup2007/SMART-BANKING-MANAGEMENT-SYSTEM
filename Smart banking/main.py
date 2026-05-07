from bank import Bank
from analytics import show_graph


def main():
    bank = Bank()

    while True:
        print("\n--- SMART BANKING SYSTEM ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Show Graph")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            bank.create_account()



        elif choice == "2":
            bank.login()

        elif choice == "3":
            show_graph()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()