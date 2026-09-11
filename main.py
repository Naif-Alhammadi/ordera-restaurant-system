import time
import os
import sys
from models.staff import Staff
from models.person import Admin
from models.storage import Storage

def main():
    print("welcome to Ordera! \na Full Restaurant System \nPlease just wait a second the System is starting up!")
    time.sleep(1)

    while True:
        display_actores_in_rest()
        actor = input("please choose your turn: ").lower()
        if actor in ["admin", "1"]:
            actor = "admin"
            user_choice(actor)
        elif actor in ["employee", "2"]:
            actor = "employee"
            user_choice(actor)
        elif actor in ["exit", "4"]:
            print("See you 👋🏼")
            sys.exit(0)


def user_choice(actor):
    match actor.lower():
        case "admin" | "1":
            while True:
                Admin.display()
                choice = input("Enter what you want: ")
                if choice in ["back", "5"]:
                    break
                admin = Admin.display_admin_cases(choice, Storage)
                print(admin)
                
            
        case "employee" | "2":
            while True:
                display_employee_choices()
                choice = input("Enter what you want: ")
                if choice.lower() in ["back", 3]:
                    break
        case "customer" | "3":
            pass
        case _:
            print("Invalid Option")

def display_actores_in_rest():
    print("\n1. Admin")
    print("2. Employee")
    print("3. Customer")
    print("4. Exit")


def display_employee_choices():
    print("\n--- Employee Menu ---")
    print("1. Send Application")
    print("2. Show Application Status")
    print("3. Back")
    print("4. Exit")


def employee_cases(choice):
    choice.lower()
    match choice:
        case "send application" | "1":
            
            Storage.save_employees_application()
        case "show status" | "2":
            pass
        case "exis" | "4":
            sys.exit(0)


if __name__ == "__main__":
    main()