from models.person import Person
from models.application import Application


class User(Person):
    def __init__(self, name, age, phone_number, address, job, experience: str):
        super().__init__(name, age, phone_number, address)
        self.experience = experience
        self.application = Application(job, "pending")


