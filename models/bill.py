from datetime import datetime
from models.employee import Employee

class Bill:
    def __init__(self, items):
        self.date = datetime.now().replace(microsecond=0)
        self.items = items
        self.status = 'pending'
        # self.id = Employee.set_id()

        