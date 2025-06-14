from abc import ABC
from account import Account

class SavingAccount(Account, ABC):

    _interest_rate = 0.0

    def __init__(self, account_number: str, account_holder_id: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(self)
        self._interest_rate = interest_rate

    #add a setter
    """ def get_interest_rate(self):
        return self._interest_rate"""

    def deposit(self, amount: float):
        if amount >= 0.0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount:float):
        if 0.0 <= amount < self._balance:
            self._balance -= amount
            return True
        return False

    def apply_interest(self):
        self._balance += self._balance * self._interest_rate

    def display_details(self) -> str:
        return super().display_details() + f", Interest Rate: {self._interest_rate}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "interest_rate": self._interest_rate,
            "type":"savings"
        })
        return data