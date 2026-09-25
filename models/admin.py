from models.person import Person
from werkzeug.security import generate_password_hash
from models.user import User


class Admin(Person):
    """" Represent an administrator with a password and ID"""

    def __init__(self, name, age, phone_number, address, password):
        """" Initialize """
        super().__init__(name, age, phone_number, address)
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


    def register_employees(self, user, register):
        if not isinstance(user, User):
            raise ValueError("Invalid Application")
        user.status = "accepted"
        

    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        phone_number = input("Enter your phone number: ")
        password = input("Enter your password: ")
        id = Person.set_id()
        return cls(name, age, phone_number, password, id)


    def __str__(self):
        return f"Name: {self.name}, Ade: {self.age}, Phone_Number: {self.phone_number}, Address: {self.address}"