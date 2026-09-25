from models.employee import Employee

class Cook(Employee):

    def job(self, bills):
        for bill in bills:
            bill.status = 'ready'
