from werkzeug.security import generate_password_hash
import csv
import random
import sys


class doesNotExit(BaseException):
    def __init__(self, message):
        super().__init__(message)

class Person:
    """" Represent a person with ID, name, age, and phone number """

    def __init__(self, id, name, age, phone_number):
        """" Initialize a Person with an ID, name, age, and phone number """
        self.id = id
        self.name = name
        self.age = age
        self.phone_number = phone_number


    # set property for Person ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if int(id) < 0:
            raise ValueError("id must be greater than 0")

        self._id = int(id)


    # set property for Person name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):

        for letter in name:
            if letter == ' ':
                continue
            elif not letter.isalpha():
                raise ValueError("name must not contain especial characters")

        self._name = name


    # set property for Person age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not Person.is_valid_age(int(age)):
            raise ValueError("age must be greater than 0 and less than 100")

        self._age = int(age)

            
    # set property for Person phone number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        # check the validtion of Yemen's phone number length
        if len(phone_number) != 16:
            raise ValueError("Number must have this format +967 7xx xxx xxx")
        spilted_phone_number = phone_number.split()
        if spilted_phone_number[0] != "+967" or spilted_phone_number[1][0:1] != "7":
            raise ValueError("Number must have this format +967 7xx xxx xxx")
        
        self._phone_number = phone_number


    @staticmethod
    def set_id():
        ids = []
        with open("uploads/ids", "r") as file:
            reader = csv.reader(file)
            ids_file = list(reader)
            id = random.choice(ids_file[0])

            for num in ids_file[0]:
                if int(num) == int(id):
                    continue
                ids.append(num)

        with open("uploads/ids", "w") as file:
            writer = csv.writer(file)
            writer.writerow(ids)

        return id

    @staticmethod
    def register():
        pass

    @staticmethod
    def login():
        pass

    @staticmethod
    def display():
        pass


    

    # check Person age validation
    @staticmethod
    def is_valid_age(age):
        if age >= 0 and age < 100:
            return True


class Admin(Person):
    """" Represent an administrator with a password """

    def __init__(self, name, age, phone_number, password, id=1):
        """" Initialize """
        super().__init__(id, name, age, phone_number)
        self.password = password

    # set property for Staff password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        for letter in password:
            if letter in [" "]:
                raise ValueError("Password must not contain spaces")
            
        self._password = generate_password_hash(password)


    @staticmethod
    def register(storage):
        if storage.save_admin(Admin.get()):
            print("You are Registered you can Login!")
            return
        return False

    @staticmethod
    def login(storage):
        try:
            return storage.load_admin("uploads/admins")
        except ValueError:
            print("You are not registered yet, Please register first.")
            raise doesNotExit("Admin does not exit")

    @staticmethod
    def display():
        print("\n--- Admin Menu ---")
        print("1. Login")
        print("2. Register")
        print("3. Show Employees Applications")
        print("4. Accept/Reject Employees Applicatons")
        print("5. Back")
        print("6. Exit")


    @staticmethod
    def display_admin_cases(choice, storage):
        choice.lower()
        match choice:
            case "login" | "1":
                return Admin.login(storage)
            case "register" | "2":
                return Admin.register(storage)
            case "Show Employees Application" | "3":
                return storage.load_employees_application()
            case "Register Employees" | "4":
                return Admin.register_employees(storage)
        
            case "exit" | "6":
                sys.exit(0)
            
    @staticmethod
    def register_employees(storage):
        applications = storage.load_employees_application()
        update_application = []
        for application in applications:
            print(application)
            apply = input("Apply? ")
            if apply.lower() in ["yes", "y"]:
                application["status"] = "accepted"
                update_application.append(application)
            elif apply.lower() in ["no", "n"]:
                application["status"] = "rejected"
                update_application.append(application)
            else:
                update_application.append(application)
            storage.update_employees_application(update_application)
    

    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        phone_number = input("Enter your phone number: ")
        password = input("Enter your password: ")
        id = Person.set_id()
        return cls(name, age, phone_number, password, id)

def main():
    naif = Person(1, "naif natheer", 21, "+967 774 556 789")


if __name__ == "__main__":
    main()