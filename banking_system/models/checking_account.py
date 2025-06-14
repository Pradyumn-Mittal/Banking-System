from abc import ABC
from account import Account

class CheckingAccount(Account, ABC):
    _overdraft_limit = 0.0

    def __init__(self, account_number: str, account_holder_id: str, initial_balance: float = 0.0, overdraft_limit: float = 0.0):
        super().__init__(self)
        self._overdraft_limit = overdraft_limit

