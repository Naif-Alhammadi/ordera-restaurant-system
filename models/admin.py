# from models.person import Person
# from werkzeug.security import generate_password_hash


# class Admin(Person):
#     """" Represent an administrator with a password and ID"""

#     def __init__(self, id, name, age, phone_number, password):
#         """" Initialize """
#         super().__init__(name, age, phone_number)
#         self.id = id
#         self.password = password

#     # set property for Staff password
#     @property
#     def password(self):
#         return self._password

#     @password.setter
#     def password(self, password):
#         for letter in password:
#             if letter in [" "]:
#                 raise ValueError("Password must not contain spaces")
            
#         self._password = generate_password_hash(password)


#     @staticmethod
#     def register(storage):
#         if storage.save_admin(Admin.get()):
#             print("You are Registered you can Login!")
#             return
#         return False

#     @staticmethod
#     def login(storage):
#         try:
#             return storage.load_admin("uploads/admins")
#         except ValueError:
#             print("You are not registered yet, Please register first.")
#             raise doesNotExit("Admin does not exit")

#     @staticmethod
#     def display():
#         print("\n--- Admin Menu ---")
#         print("1. Login")
#         print("2. Register")
#         print("3. Show Employees Applications")
#         print("4. Accept/Reject Employees Applicatons")
#         print("5. Back")
#         print("6. Exit")


#     @staticmethod
#     def display_admin_cases(choice, storage):
#         choice.lower()
#         match choice:
#             case "login" | "1":
#                 return Admin.login(storage)
#             case "register" | "2":
#                 return Admin.register(storage)
#             case "Show Employees Application" | "3":
#                 return storage.load_employees_application()
#             case "Register Employees" | "4":
#                 return Admin.register_employees(storage)
        
#             case "exit" | "6":
#                 sys.exit(0)
            
#     @staticmethod
#     def register_employees(storage):
#         applications = storage.load_employees_application()
#         update_application = []
#         for application in applications:
#             print(application)
#             apply = input("Apply? ")
#             if apply.lower() in ["yes", "y"]:
#                 application["status"] = "accepted"
#                 update_application.append(application)
#             elif apply.lower() in ["no", "n"]:
#                 application["status"] = "rejected"
#                 update_application.append(application)
#             else:
#                 update_application.append(application)
#             storage.update_employees_application(update_application)
    

#     @classmethod
#     def get(cls):
#         name = input("Enter your name: ")
#         age = input("Enter your age: ")
#         phone_number = input("Enter your phone number: ")
#         password = input("Enter your password: ")
#         id = Person.set_id()
#         return cls(name, age, phone_number, password, id)