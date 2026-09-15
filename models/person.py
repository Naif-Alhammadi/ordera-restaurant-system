from models.address import Address

import csv
import sys


class doesNotExit(BaseException):
    def __init__(self, message):
        super().__init__(message)

class Person:
    """" Represent a person with name, age, and phone number """

    def __init__(self, name, age, phone_number, address):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.address = address

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


    # set property for Person address
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        if not isinstance(address, Address):
            raise ValueError("Invalid Address")
        self._address = address


    # check Person age validation
    @staticmethod
    def is_valid_age(age):
        if age >= 0 and age < 100:
            return True




def main():
    naif = Person(1, "naif natheer", 21, "+967 774 556 789")


if __name__ == "__main__":
    main()