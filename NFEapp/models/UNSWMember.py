from .Course import *
from .Seminar import *
from .Member import *
from datetime import datetime

class UNSWMember(Member):

    def __init__ (self, username, zID, email, password, role):
        super().__init__(username, password)
        self._zID = zID
        self._email = email
        self._role = role

    #getters
    @property
    def zID(self):
        return self._zID

    @property
    def email(self):
        return self._email

    @property
    def role(self):
        return self._role

    #setters
    @email.setter
    def email(self, email):
        self._email = email

    @role.setter
    def role(self, role):
        valid_role = ['trainer', 'trainee']
        if role in valid_role:
            self._role = role
            return 1
        else:
            return 0

    def __str__(self):
        return "name: {0}, email: {1}".format(self._username, self._email)

    def is_guest(self):
        return False
