from models.address import Address


class Restaurant:
    def __init__(self):
        self.name = "Ordera Restaurant"
        self.address = Address('Sana''a', 'Yemen', '60 meter Rd')
        self.table_counts = 5

    @property
    def table_counts(self):
        return self._table_counts

    @table_counts.setter
    def table_counts(self, counts):
        if counts < 0:
            raise ValueError("Invalid Count")
        self._table_counts = counts

    def buy_tables(self, count):
        self._table_counts += count

    def reserve_table(self):
        self.table_counts -= 1


    def __str__(self):
        return f"{self.name}, - Address - {self.address}, Tables: {self.table_counts}"