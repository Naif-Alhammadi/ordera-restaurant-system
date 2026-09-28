from models.menu.menu import Menu

class Order:
    def __init__(self, orders, takeaway=True):
        self.order = orders
        self.type = takeaway
        self.menu = Menu()
        # self.total_amount = 0

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, orders):
        if not isinstance(orders, list):
            raise TypeError("Invalid Order List")
        self._order = orders

    def is_valid_order(self, orders):
        for order in orders:
            if order.lower() not in self.menu.food and order.lower() not in self.menu.drink:
                raise ValueError("Invalid Order")
        return True

    def total_amount(self, orders):
        total = 0
        for order in orders:
            if order in self.menu.food:
                total += self.menu.food.get(order)
            elif order in self.menu.drink:
                total += self.menu.drink.get(order)

        return total

    def dine_in(self):
        if self.type:
            return False
        return True



