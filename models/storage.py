import csv
from werkzeug.security import check_password_hash, generate_password_hash
from models.person import Admin
import os

PASSWORD = 123

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

        # Return expetion if Admin not found in the file
        else:
            print("There is no Admin named like that")
            raise Reject("There is no Admin named like that")
            

    @staticmethod
    def save_admin(admin):
        os.makedirs("uploads", exist_ok=True)
        with open("uploads/admins", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "admin", "age", "phone", "hash"])
            writer.writeheader()                        
            program_passwrod = input("Enter The Program Password: ")
            if int(program_passwrod) == PASSWORD:
                writer.writerow({"ID": admin.id,"admin": admin.name, "age": admin.age, "phone": admin.phone_number,"hash": admin.password})

    @staticmethod
    def load_employees_application():
        try:
            with open("uploads/employees_application", "r") as file:
                reader = csv.DictReader(file)
                application = list(reader)

        except FileNotFoundError:
            raise FileNotFoundError("not found") 

        return application
        


    @staticmethod
    def employees_application(employee):
        os.makedirs("uploads", exist_ok=True)
        with open("uploads/employees_application", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "age", "experience", "message", "status"])
            writer.writeheader()
            writer.writerow({"name": employee.name, "age": employee.age, "experience": employee.experience, "message": employee.message, "status": employee.status})

    @staticmethod
    def save_employees_application(employee):
        os.makedirs("upload", exist_ok=True)
        with open("upload/employees_application", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "age" , "experience" , "message", "status"])
            writer.writerow({"name": employee.name, "age": employee.age, "experience": employee.experience, "message": employee.message, "status": employee.status})

        @staticmethod
        def update_employees_application(updated_application):
            with open("upload/employees_application", "w") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "age" , "experience" , "message", "status"])
                writer.writerow({{"name": employee.name, "age": employee.age, "experience": employee.experience, "message": employee.message, "status": employee.status}})
