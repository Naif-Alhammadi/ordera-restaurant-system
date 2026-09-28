from datetime import datetime

class Bill:
    def __init__(self, items):
        self.date = datetime.now().replace(microsecond=0)
        self.items = items
        self.status = 'pending'