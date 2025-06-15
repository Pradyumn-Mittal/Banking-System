from .account import Account

class CheckingAccount(Account):
    def __init__(self, account_number: str, account_holder_id: str, initial_balance: float = 0.0, overdraft_limit: float = 0.0):
        super().__init__(account_number, account_holder_id, initial_balance)
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, new_limit):
        self._overdraft_limit = new_limit

    def deposit(self, amount: float) -> bool:
        if amount > 0.0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount:float) -> bool:
        if 0.0 < amount and  self._balance - amount >= -self._overdraft_limit:
            self._balance -= amount
            return True
        return False

    def display_details(self) -> str:
        details = super().display_details() + f", Interest Rate: {self._overdraft_limit}"
        return details

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "overdraft_limit": self._overdraft_limit,
            "type":"checking"
        })
        return data