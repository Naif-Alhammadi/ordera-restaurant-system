from models.employee import Employee

class Waiter(Employee):
    def __init__(self, user, user_account=0):
        super().__init__(user, user_account)
        self.bills = list()


    def job(self, customer_id, bill):
        self.bills.append({bill:customer_id})
        if bill.status != 'pending':
            return True
        return False
