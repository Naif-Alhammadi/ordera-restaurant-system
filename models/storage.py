import csv
from werkzeug.security import check_password_hash, generate_password_hash
from models.person import Admin
import os

class Reject(BaseException):
    def __init__(self, message):
        super().__init__(message)

class Storage:
    @staticmethod
    def load_admin(path):
        try:
            with open(path, "r") as file:
                reader = csv.DictReader(file)
                data = list(reader)

        except FileNotFoundError:
            raise Reject("request has been rejected")

        name = input("Enter Your Name: ")
        password = input("Enter Your Password: ")
        for line in data:
            if line["admin"] == name:
                if check_password_hash(line["hash"], password):
                    age = line["age"]
                    ID = line["ID"]
                    phone_number = line["phone"]
                    return Admin(name, age, phone_number, password, ID)

        # Return expetion will be add later
        else:
            raise Reject("There is no Admin named like that")
            

    @staticmethod
    def save_admin(admin):
        os.makedirs("uploads", exist_ok=True)
        with open("uploads/admins", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "admin", "age", "phone", "hash"])
            writer.writeheader()
            writer.writerow({"ID": admin.id,"admin": admin.name, "age": admin.age, "phone": admin.phone_number,"hash": admin.password})


    # @staticmethod
    # def employees_application(sender, message, application_status = "pending"):
    #     os.makedirs("uploads", exist_ok=True)
    #     with open("uploads/employees_application", "w") as file:
    #         writer = csv.DictWriter(file, fieldnames=["name", "age", "experience", "message", "status"])
    #         writer.writeheader()
    #         writer.writerow({"name": sender.name, "age": sender.age, "experience": sender.experience, "message": message, "status": application_status})