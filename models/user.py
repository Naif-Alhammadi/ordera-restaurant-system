from models.person import Person
from models.application import Application


class User(Person):
    def __init__(self, name, age, phone_number, address, job, experience: str):
        super().__init__(name, age, phone_number, address)
        self.experience = experience
        self.job = job
        self.application = Application(job, "pending")

    def __str__(self):
        return f"Sender_Name: {self.name}, Age: {self.age}, Address: {self.address}, want_to_be_a: {self.job} With_the_experience: {self.experience}, Status: {self.application.status}"