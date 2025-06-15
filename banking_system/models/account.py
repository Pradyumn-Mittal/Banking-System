from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number: str, account_holder_id: str, initial_balance: float = 0.0):
        self._account_number: str = account_number
        self._balance: float = initial_balance
        self._account_holder_id: str = account_holder_id

    @property
    def account_number(self):
        return self._account_number

    @property
    def initial_balance(self):
        return self._balance

    @property
    def account_holder_id(self):
        return self._account_holder_id

    @abstractmethod
    def deposit(self, amount: float) -> bool:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass

    def display_details(self) -> str:
        return f"Acc. No: {self._account_number}, Balance: ${self._balance}"

    def to_dict(self) -> dict:
        return {
            "account_number": self._account_number,
            "account_holder_id": self._account_holder_id,
            "balance": self._balance,
            "type": "generic"
        }
