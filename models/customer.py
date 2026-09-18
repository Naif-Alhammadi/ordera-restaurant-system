class Customer:
    def __init__(self, account):
        self.account = account

    @property
    def account(self):
        return self._account

    @property
    def account(self, account):
        if account < 0:
            raise ValueError("Invalid Account Amount")
        self.account = account

    def order_payment(self, price):
        if price > self.account:
            return False
        return True   
