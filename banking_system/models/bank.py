import json
import os
import uuid

from .customer import Customer
from .account import Account
from .saving_account import SavingAccount
from .checking_account import CheckingAccount

class Bank:
    def __init__(self, customer_file='data/customers.json', account_file='data/accounts.json'):
        self._customers = {}
        self._accounts = {}
        self._customer_file = customer_file
        self._account_file = account_file
        self.__load_data()

    def __load_data(self) -> None:
        if os.path.exists(self._customer_file):
            with open(self._customer_file, 'r') as f:
                customer_data = json.load(f)
                for cid, data in customer_data.items():
                    customer = Customer(data['customer_id'], data['name'], data['address'])
                    for acc_num in data.get('account_numbers', []):
                        customer.add_account_number(acc_num)
                    self._customers[cid] = customer

        if os.path.exists(self._account_file):
            with open(self._account_file, 'r') as f:
                account_data = json.load(f)
                for aid, data in account_data.items():
                    account_type = data.get('type')
                    if account_type == 'savings':
                        account = SavingAccount(
                            data['account_number'],
                            data['account_holder_id'],
                            data['balance'],
                            data.get('interest_rate', 0.01)
                        )
                    elif account_type == 'checking':
                        account = CheckingAccount(
                            data['account_number'],
                            data['account_holder_id'],
                            data['balance'],
                            data.get('overdraft_limit', 0.0)
                        )
                    else:
                        print(f"Unknown account type: {account_type}")
                        continue
                    self._accounts[aid] = account

    def __save_data(self) -> None:
        with open(self._customer_file, 'w') as f:
            json.dump({cid: cust.to_dict() for cid, cust in self._customers.items()}, f, indent=4)

        with open(self._account_file, 'w') as f:
            json.dump({aid: acc.to_dict() for aid, acc in self._accounts.items()}, f, indent=4)

    def add_customer(self, customer: Customer) -> bool:
        if customer.customer_id in self._customers:
            return False
        self._customers[customer.customer_id] = customer
        self.__save_data()
        return True

    def remove_customer(self, customer_id: str) -> bool:
        if customer_id not in self._customers:
            return False
        self._customers.pop(customer_id)
        self.__save_data()
        return True

    def create_account(self, customer_id: str, account_type: str, initial_balance: float = 0.0, **kwargs) -> Account | None:
        if customer_id not in self._customers:
            return None

        account_number = str(uuid.uuid4())
        if account_type == 'savings':
            account = SavingAccount(account_number, customer_id, initial_balance, kwargs.get('interest_rate', 0.01))
        elif account_type == 'checking':
            account = CheckingAccount(account_number, customer_id, initial_balance, kwargs.get('overdraft_limit', 0.0))
        else:
            print(f"Invalid account type: {account_type}")
            return None

        self._accounts[account_number] = account
        self._customers[customer_id].add_account_number(account_number)
        self.__save_data()
        return account

    def deposit(self, account_number: str, amount: float) -> bool:
        account = self._accounts.get(account_number)
        if account and account.deposit(amount):
            self.__save_data()
            return True
        return False

    def withdraw(self, account_number: str, amount: float) -> bool:
        account = self._accounts.get(account_number)
        if account and account.withdraw(amount):
            self.__save_data()
            return True
        return False

    def transfer_funds(self, from_acc_num: str, to_acc_num: str, amount: float) -> bool:
        if self.withdraw(from_acc_num, amount) and self.deposit(to_acc_num, amount):
            return True
        return False

    def get_customer_accounts(self, customer_id: str) -> list[Account]:
        customer = self._customers.get(customer_id)
        if not customer:
            return []
        return [self._accounts[acc_num] for acc_num in customer.account_numbers if acc_num in self._accounts]

    def display_all_customers(self) -> None:
        for customer in self._customers.values():
            print(customer.display_details())

    def display_all_accounts(self) -> None:
        for account in self._accounts.values():
            print(account.display_details())

    def apply_all_interest(self) -> None:
        for account in self._accounts.values():
            if hasattr(account, 'apply_interest'):
                account.apply_interest()
        self.__save_data()
