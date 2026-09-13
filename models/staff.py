from models.person import Person
from models.storage import Storage
import sys


class lengthError(BaseException):
    def __init__(self, message):
        super().__init__(message)


class Staff(Person):
    """" Represent Staff class a subclass of Person that additionally take password """

    def __init__(self, id, name, age, phone_number, experience, message,status="pending"):
        """" Initialize """
        super().__init__(id, name, age, phone_number)
        self.experience = experience
        self.status = status
        self.storage = Storage()
        self.message = message


    # set property for Staff experience
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        if len(experience) >= 0 and len(experience) <= 100:
            raise ValueError("Experience must have a length of 30 and smaller than 100")
        self._experience = experience

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status not in ["pending", "accepted", "rejected"]:
            raise ValueError("value does not exits")
        self._status = status


    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        if len(message) > 50:
            raise lengthError("length is greater than 50")
        self._message = message


    @staticmethod
    def display_employee_choices():
        print("\n--- Employee Menu ---")
        print("1. Send Application")
        print("2. Show Application Status")
        print("3. Back")
        print("4. Exit")

    @staticmethod
    def employee_cases(choice):
        choice.lower()
        match choice:
            case "send application" | "1":
                employee = Staff.get()
                Staff.send_application(employee)
            case "show status" | "2":
                name = input("Enter your name: ")
                employee_applications = Storage.load_employees_application()
                print(employee_applications)
                for employee in employee_applications:
                    print("hi")
                    print(employee)
                    if employee["name"] == name:
                        # not working need to fix
                        age = employee["age"]
                        experience = employee["experience"]
                        message = employee["message"]
                        phone_number = "+967 774 556 789"
                        employee =  Staff(name, age, message, phone_number, experience, message)
                        print(employee._status)
                        return
                print("You have not send any application yet")

            case "exis" | "4":
                sys.exit(0)
            case _:
                pass

            


    @staticmethod
    def send_application(employee):
        Storage.save_employees_application(employee)

    def account(self):
        ...

    def job(self):
        ...

    @classmethod
    def get(cls):
        name = input("name: ")
        age = input("age: ")
        phone_number = input("phone_number: ")
        experience = input("experience: ")
        message = input("enter a message if you wish: ")
        id = Staff.set_id()

        return cls(id, name, age, phone_number, experience, message)


def main():
    pass

if __name__ == "__main__":
    main()