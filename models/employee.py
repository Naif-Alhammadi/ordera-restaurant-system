from models.user import User
from abc import ABC, abstractmethod
import csv


class lengthError(BaseException):
    def __init__(self, message):
        super().__init__(message)


class Employee(ABC):
    """" Represent Staff class a subclass of Person that additionally take password """

    def __init__(self, user, user_account=0):
        self.__id = Employee.set_id()
        self.user = user
        self.user_account = user_account

    @property
    def id(self):
        return self.__id

    @property
    def user_account(self):
        return self.__user_account

    @user_account.setter
    def user_account(self, user_account):
        if user_account < 0:
            raise ValueError("Invalid Amount")
        self.__user_account = user_account

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if not isinstance(user, User):
            raise ValueError("Invalid user")
        self._user = user

    @staticmethod
    def set_id():
        ids = []
        with open("uploads/ids", "r") as file:
            reader = csv.reader(file)
            ids_file = list(reader)
            id = ids_file[0][0]

            for num in ids_file[0]:
                if int(num) == int(id):
                    continue
                ids.append(num)

        with open("uploads/ids", "w") as file:
            writer = csv.writer(file)
            writer.writerow(ids)

        return id

    # @abstractmethod
    def job(self):
        pass



def main():
    pass

if __name__ == "__main__":
    main()