class Person:
    def __init__(self, id, name, age, phone_number):
        self.id = id
        self.name = name
        self.age = age
        self.phone_number = phone_number

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id < 0:
            raise ValueError("id must be greater than 0")

        self._id = id


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
            

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if len(phone_number) != 16:
            raise ValueError("Number must have this format +967 7xx xxx xxx")
        spilted_phone_number = phone_number.split()
        if spilted_phone_number[0] != "+967" or spilted_phone_number[1][0:1] != "7":
            raise ValueError("Number must have this format +967 7xx xxx xxx")



    @staticmethod
    def is_valid_age(age):
        if age <= 0:
            raise ValueError("age must be grater than 0")


def main():
    naif = Person(1, "naif natheer", 21, "+967 774 556 789")
    Person.is_valid_age(naif.age)


if __name__ == "__main__":
    main()