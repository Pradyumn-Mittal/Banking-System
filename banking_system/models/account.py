import abc

class Account(abc):

    _account_number = ""
    _balance = 0
    _account_holder_id = ""

    def __init__(self, account_number: str, account_holder_id: str, initial_balance: float = 0.0):
        self._account_number = account_number
        self._balance = initial_balance
        self._account_holder_id = account_holder_id

    @property
    def account_number(self):
        return self._account_number

    @property
    def initial_balance(self):
        return self._balance

    @property
    def account_holder_id(self):
        return self._account_holder_id

