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
        if id < 0:
            raise ValueError("id must be greater than 0")

        self._id = id


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
        if not Person.is_valid_age(age):
            raise ValueError("age must be greater than 0 and less than 100")

        self._age = age 

            
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


    # check Person age validation
    @staticmethod
    def is_valid_age(age):
        if age >= 0 and age < 100:
            return True


def main():
    naif = Person(1, "naif natheer", 21, "+967 774 556 789")


if __name__ == "__main__":
    main()