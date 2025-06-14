from customer import Customer
from account import Account

class Bank:
    def __init__(self, customer_file='data/customers.json', account_file='data/accounts.json'):
        self._customers = {}  # customer_id -> Customer object
        self._accounts = {}   # account_number -> Account object
        self._customer_file = customer_file
        self._account_file = account_file
        self.__load_data()

    def __load_data(self) -> None:
        pass

    def __save_data(self) -> None:
        pass

    def add_customer(self, customer: "Customer") -> bool:
        if customer in self._customers:
            return False

        self._customers[customer.customer_id] = customer
        self.__save_data()
        return True


    def remove_customer(self, customer_id: str) -> bool:
        if customer_id not in self._customers:
            return False
        self._customers.pop(customer_id)
        return True

    def create_account(self, customer_id: str, account_type: str, initial_balance: float = 0.0, ** kwargs) -> Account | None:
        pass

    def deposit(self, account_number: str, amount: float):
        pass

    def withdraw(self, account_number: str, amount: float):
        pass

    def transfer_funds(self, from_acc_num: str, to_acc_num: str, amount: float) -> bool:
        pass

    def get_customer_accounts(self, customer_id: str)-> list[Account]:
        pass

    def display_all_customers(self) -> None:
        pass

    def display_all_accounts(self) -> None:
        pass

    def apply_all_interest(self) -> None:
        pass
