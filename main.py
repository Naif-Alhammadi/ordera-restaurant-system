import time
import os
from models.staff import Staff
from models.person import Admin
from models.storage import Storage


def main():
    print("welcome to Ordera! \na Full Restaurant System \nPlease just wait a second the System is starting up!")
    time.sleep(1)
    actores_in_rest()
    actor = input("please choose your turn: ")
    if choose_user(actor) == None:
        actor = input("please choose your turn: ")


def choose_user(actor):
    match actor.lower():
        case "admin":
            try:
                return Storage.load_admin("uploads/admins")
            except:
                return None
        case "employee":
            return
        case "customer":
            return
        case _:
            return

def actores_in_rest():
    print("1. Admin")
    print("2. Employee")
    print("3. Customer")

if __name__ == "__main__":
    main()