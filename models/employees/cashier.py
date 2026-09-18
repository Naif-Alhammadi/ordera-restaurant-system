from models.employee import Employee
from models.account import Account
from models.customer import Customer

class Cashier(Employee):
    def __init__(self, user, account, user_account=0):
        super().__init__(user, user_account)
        self.account = account
        self.money_earned = 0


    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        if not isinstance(account, Account):
            raise ValueError("Invalid Account")
        self._account = account
    


    @property
    def money_earned(self):
        return self._money_earned

    @money_earned.setter
    def money_earned(self, money=0):
        if money < 0:
            raise ValueError("Invalid Money Amount")
        self._money_earned = money

    def job(self, money):
        self.account.daily_earnings += money
        self.account.total_earnings += self._money_earned
        self._money_earned = 0
