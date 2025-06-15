import uuid

from loading.loading import Loading
from models.bank import Bank
from models.customer import Customer


def main():
    bank = Bank()

    while True:

        load = Loading()

        print("\nBanking System Menu:")
        print("1. Add Customer")
        print("2. Remove Customer")
        print("3. Create Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer Funds")
        print("7. View Customer Accounts")
        print("8. Apply Interest")
        print("9. Display All Customers")
        print("10. Display All Accounts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            customer_id = str(uuid.uuid4())
            customer = Customer(customer_id, name, address)
            if bank.add_customer(customer):
                print("Customer added successfully.")
            else:
                print("Customer already exists.")

        elif choice == '2':
            print()
            customer_id = input("Enter customer ID to remove: ")
            if bank.remove_customer(customer_id):
                print("Customer removed successfully.")
            else:
                print("Customer not found or has associated accounts.")

        elif choice == '3':
            print()
            customer_id = input("Enter customer ID: ")
            account_type = input("Enter account type (savings/checking): ")
            initial_balance = float(input("Enter initial balance: "))
            kwargs = {}
            if account_type == 'savings':
                kwargs['interest_rate'] = float(input("Enter interest rate: "))
            elif account_type == 'checking':
                kwargs['overdraft_limit'] = float(input("Enter overdraft limit: "))
            account = bank.create_account(customer_id, account_type, initial_balance, **kwargs)
            if account:
                print(f"{account_type.capitalize()} account created successfully.")
            else:
                print("Failed to create account.")

        elif choice == '4':
            print()
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if bank.deposit(account_number, amount):
                print("Deposit successful.")
            else:
                print("Failed to deposit.")

        elif choice == '5':
            print()
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if bank.withdraw(account_number, amount):
                print("Withdrawal successful.")
            else:
                print("Failed to withdraw.")

        elif choice == '6':
            print()
            from_acc_num = input("Enter source account number: ")
            to_acc_num = input("Enter destination account number: ")
            amount = float(input("Enter amount to transfer: "))
            if bank.transfer_funds(from_acc_num, to_acc_num, amount):
                print("Transfer successful.")
            else:
                print("Failed to transfer funds.")

        elif choice == '7':
            print()
            customer_id = input("Enter customer ID: ")
            accounts = bank.get_customer_accounts(customer_id)
            if accounts:
                for account in accounts:
                    print(account.display_details())
            else:
                print("No accounts found for this customer.")

        elif choice == '8':
            print()
            bank.apply_all_interest()
            print("Interest applied to all savings accounts.")

        elif choice == '9':
            print()
            bank.display_all_customers()

        elif choice == '10':
            print()
            bank.display_all_accounts()

        elif choice == '0':
            load.loading_anim("Exiting.....", 5)
            return

        else:
            print("Invalid choice. Please try again.")

        load.loading_anim("Going Back to Main Menu..........", 10)


if __name__ == "__main__":
    main()
