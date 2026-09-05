from models.person import Person
import utils.save

class Staff(Person):
    """" Represent Staff class a subclass of Person that additionally take password """

    def __init__(self, id, name, age, phone_number, experience):
        """" Initialize """
        super().__init__(id, name, age, phone_number)
        self.experience = experience


    # set property for Staff experience
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        if len(experience) >= 0 and len(experience) <= 100:
            raise ValueError("Experience must have a length of 30 and smaller than 100")
        self._experience = experience

    def send_application(self, message):
        utils.save.employees_application(self, message)

    def account(self):
        ...

    def job(self):
        ...


def main():
    pass

if __name__ == "__main__":
    main()