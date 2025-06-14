class Customer:

    def __init__(self, customer_id: str, name: str, address: str):
        self._customer_id = customer_id
        self._name = name
        self._address = address
        self._account_numbers = [""]

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def name(self):
        return self._name

    @property
    def account_numbers(self):
        return self._account_numbers.copy()

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address

    def add_account_number(self, account_number: str) -> None:
        if account_number not in self._account_numbers:
            self._account_numbers.append(account_number)

    def remove_account_number(self, account_number: str) -> None:
        if account_number in self._account_numbers:
            self._account_numbers.remove(account_number)

    def display(self) -> str:
        return f"Customer ID: {self._customer_id}, Name: {self._name}, Address: {self._address}, No. of Acc.: {len(self._account_numbers)}"

    def to_dict(self) -> dict:
        details = {
            "customer_id": self._customer_id,
            "name":self._name,
            "address":self._address,
            "account_numbers":self._account_numbers
        }
        return details
