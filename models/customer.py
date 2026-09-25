class Customer:
    def __init__(self, account):
        self.account = account
        self.finish = False

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        if account < 0:
            raise ValueError("Invalid Account Amount")
        self._account = account

    def order_payment(self, price):
        if price > self.account:
            return False
        return True   
