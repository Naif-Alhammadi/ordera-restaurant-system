from models.menu.food import Food
from models.menu.drink import Drink

class Menu:
    def __init__(self):
        self.food = Food.LIST
        self.drink = Drink.LIST

    def __str__(self):
        menu = ""
        menu += "--Foods-- \n"
        for food in self.food:
            menu += food + " " + str(self.food[food]) + "" + "\n"
        menu += "--Drinks-- \n"
        for drink in self.drink:
            menu += drink + " " + str(self.drink[drink]) + "\n"
        return f"\n------Menu------\n{menu}"