from models.user import User
from abc import ABC, abstractmethod


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
        ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        id = ids[0]
        ids.remove(id)

        return id

    @abstractmethod
    def job(self):
        pass

    def __str__(self):
        return f"name: {self.user}, has: {self.user_account}"



def main():
    pass

if __name__ == "__main__":
    main()