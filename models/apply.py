from datetime import datetime
from models.application import Application
from models.user import User


class Apply:
    """" Represent an Apply with a application date"""

    def __init__(self, application, user):
        self.date = datetime.now().replace(microsecond=0)
        self.application = application
        self.user = user

    @property
    def application(self):
        return self._application

    # set property for application
    @application.setter
    def application(self, application):
        if not isinstance(application, Application):
            raise ValueError("Invalid Application")

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if not isinstance(user, User):
            raise ValueError("Invalid user")
        self._user = user

    def __str__(self):
        return f"user {self.user.name} applied on {self.date} and the status is {self.user.application.status}"
        


        