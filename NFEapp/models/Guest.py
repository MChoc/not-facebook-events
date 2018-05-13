from .Member import *

class Guest(Member):

    def __init__(self, username, password, email):
        super().__init__(username, password)
        self._email = email
        self._role = 'Guest'
        self._currentEvents = []
        self._pastEvents = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def currentEvents(self):
        return self._currentEvents

    @property
    def pastEvents(self):
        return self._pastEvents
