import time
import os
from models.staff import Staff
from models.person import Admin
from models.storage import Storage
from models.storage import Reject


def main():
    print("welcome to Ordera! \na Full Restaurant System \nPlease just wait a second the System is starting up!")
    time.sleep(1)
    actores_in_rest()
    while True:
        actor = input("please choose your turn: ")
        turn = choose_user(actor)
        if turn == "Exit":
            break
        actores_in_rest()


def choose_user(actor):
    match actor.lower():
        case "admin" | "1":
            try:
                return Storage.load_admin("uploads/admins")
            except Reject:
                register = input("you are not registered do you want to register? yes/no : ")
                if register.lower() in ["yes", "y"]:
                    admin = Admin.get()
                    Storage.save_admin(admin)
                    return admin
                return None
        case "employee" | "2":
            return
        case "customer" | "3":
            return
        case "exit" | "4":
            return "Exit"
        case _:
            return

def actores_in_rest():
    print("1. Admin")
    print("2. Employee")
    print("3. Customer")
    print("4. Exit")

if __name__ == "__main__":
    main()