import time
import sys

from models.admin import Admin
from models.address import Address
from models.apply import Apply
from models.account import Account
from models.bill import Bill
from models.employees.cashier import Cashier
from models.employees.cook import Cook
from models.customer import Customer
from models.menu.menu import Menu
from models.order import Order
from models.user import User
from models.restaurant import Restaurant
from models.employees.waiter import Waiter

# for each employee in the restaurnt
CASHIERS = []
WAITERS = []
COOKS = []


def main():
    print("welcome to Ordera! \na Full Restaurant System \nPlease just wait a second the System is starting up!")

    # initial objects
    obj_rest, obj_admin, account, menu, obj_user1, obj_user2, obj_user3 = start()
    users = {"user1": obj_user1, "user2": obj_user2, "user3": obj_user3}
    time.sleep(1)

    # keep truck of user input
    while True:
        display_actores_in_rest()
        actor = input("please choose your turn: ").lower()
        if actor in ["admin", "1"]:
            user_choice(actor, obj_admin, users)

        elif actor in ["user", "2"]:
            user_choice(actor, obj_admin, users)

        elif actor in ["restaurant", "3"]:
            print(obj_rest)

            #display restaurant menu
            print("----Menu-----")

            # display restaurant employees
            print(menu)
            print("----Employees-----")
            try:
                print(CASHIERS[0])
                print(WAITERS[0])
                print(COOKS[0])
            except IndexError:
                print("No Employees at This Time Please Ask the Admin to add Employees First")

        elif actor in ["customer", "4"]:

            # check if the restaurant has employees
            while True:
                try:
                    CASHIERS[0]
                    WAITERS[0]
                    COOKS[0]
                except IndexError:
                    print("No Employees at This Time Please Ask the Admin to add Employees First")
                    break

                # initial curomer object and take its orders
                customer = Customer(1000)
                print(menu)
                orders = []
                print("press q to finish your order")
                customer_order = input("Your order: ")

                # keep taking cusomer orders until it press q
                while customer_order != "q":
                    orders.append(customer_order)
                    customer_order = input("Your order: ")

                # check order status
                takeaway = input("Takeaway? yes/no: ").lower()
                if takeaway in ["y", "yes"]:
                    order = Order(orders)
                else:
                    order = Order(orders, False)

                # check if user order a valid orders
                order.is_valid_order(orders)

                # take presmission from the cusomer to pay the order bill
                print("Your Order Amount is: ", order.total_amount(orders))
                pay = input("pay it? yes/no ").lower()
                print(pay)
                if pay in ["y", "yes"]:
                    if order.total_amount(orders) > customer.account:
                        print("you can not offer this")
                        break
                    else:
                        # cashier takes the amount and add to the restaurant account
                        customer.account = customer.account - order.total_amount(orders)
                        print("Your amount after paid the bill = ", customer.account)
                        CASHIERS[0].job(order.total_amount(orders))
                        bill = Bill(orders)
                        break


        elif actor in ["exit", "5"]:
            print("See you 👋🏼")
            print(CASHIERS, WAITERS, COOKS)
            sys.exit(0)


# keep truck of actor input
def user_choice(actor, admin, user):
    match actor.lower():
        case "admin" | "1":
            while True:
                display_admin_cases()
                choice = input("Enter what you want: ")
                if choice in ["back", "3"]:
                    break
                admin_cases(choice, admin, user)
                
            
        case "user" | "2":
            
            while True:
                display_user_cases()
                choice = input("Enter what you want: ")
                if choice in ["back", "3"]:
                    break
                user_cases(choice, user)

        case _:
            print("Invalid Option")


# display validate choices of the program
def display_actores_in_rest():
    print("\n1. Admin")
    print("2. User")
    print("3. Restaurant")
    print("4. Customer")
    print("5. Exit")


# display validate choices for Admins
def display_admin_cases():
    print("\n----- Admin -----")
    print("1. Show Admin Info")
    print("2. Register Employee")
    print("3. Back")
    print("4. Exit")


# display validate choices for Users
def display_user_cases():
    print("\n----- User -----")
    print("1. Show Users Info")
    print("2. Show Applied Applications")
    print("3. Back")
    print("4. Exit")


# valid choices to the Admins
def admin_cases(choice, admin, users):
    match choice:
        case "show" | "1":
            print(admin)

        case "register" | "2":
            for user in users:
                print(users[user])
                register = input("Register it? yes/no: ").lower()
                if register in ["y", "yes"]:
                    users[user].application.status = "accepted"
                if users[user].application.status == "accepted":
                    match users[user].application.job.lower():
                        case "cook":
                            cook = Cook(users[user])
                            COOKS.append(cook)

                        case "waiter":
                            waiter = Waiter(users[user])
                            WAITERS.append(waiter)

                        case "cashier":
                            account = Account()
                            cashier = Cashier(users[user], account)
                            CASHIERS.append(cashier)                
            return
        

        case "exit" | "4":
            sys.exit(0)
            

# valid choices to the Users
def user_cases(choice, users):
    match choice:
        case "show" | "1":
            for user in users:
                print(users[user])

        case "register" | "2":
            for user in users:
                apply = Apply(users[user].application, users[user])
                print(apply)

        case "exit" | "4":
            sys.exit(0)


# intitial objects
def start():
    address_emp = Address("Sana'a", "Yemen", "60 meters Rd")
    address_admin = Address("Sana'a", "Yemen", "60 meters Rd")

    admin = Admin("Naif", 21, "+967 774 550 000", address_admin, "123")
    restaurant = Restaurant()
    user_cook = User("Ahmed", 22, "+967 777 000 000", address_emp, "cook", "cooked in many restaurant")
    user_waiter = User("Aiman", 22, "+967 777 000 000", address_emp, "waiter", "cooked in many restaurant")
    user_cashier = User("Mustafa", 22, "+967 777 000 000", address_emp, "cashier", "cooked in many restaurant")
    menu = Menu()
    account = Account()

    return restaurant, admin, account, menu, user_cook, user_waiter, user_cashier


if __name__ == "__main__":
    main()