import time
import os
import sys
from models.staff import Staff
from models.person import Admin
from models.storage import Storage
from models.storage import Reject


def main():
    print("welcome to Ordera! \na Full Restaurant System \nPlease just wait a second the System is starting up!")
    time.sleep(1)

    while True:
        actores_in_rest()
        actor = input("please choose your turn: ")
        if actor in ["admin", "1"]:
            actor = "admin"
            choose_user(actor)
        elif actor in ["exit", "4"]:
            print("See you 👋🏼")
            break


def choose_user(actor):
    match actor.lower():
        case "admin" | "1":
            display()
            while True:
                choice = input("Enter what you want: ")
                if choice in ["back", "3"]:
                    break

                display_admin_cases(choice)
                
            
        case "employee" | "2":
            pass
        case "customer" | "3":
            pass
        case _:
            print("Invalid Option")

def actores_in_rest():
    print("\n1. Admin")
    print("2. Employee")
    print("3. Customer")
    print("4. Exit")

def display():
    print("\n--- Admin Menu ---")
    print("1. Login")
    print("2. Register")
    print("3. Back")
    print("4. Exit")

def display_admin_cases(choice):
    choice.lower()
    match choice:
        case "login" | "1":
            return login("admin")
        case "register" | "2":
            return register("admin")
        case "exit" | "4":
            sys.exit(0)



def register(actor):
    if actor == "admin":
            admin = Admin.get()
            Storage.save_admin(admin)
            print("You are all set you can Login!")
            return admin
    

def login(actor):
    if actor == "admin":
            try:
                return Storage.load_admin("uploads/admins")
            except Reject:
                register = input("You are not registered yet, Please register first. Register? yes/no : ")
    
                if register.lower() in ["yes", "y"]:    
                    return login("admin")
                else:
                    return choose_user("admin")


if __name__ == "__main__":
    main()