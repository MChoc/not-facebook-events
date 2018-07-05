from .Member import *
from .Course import *
from .Seminar import *
from datetime import datetime

class Guest(Member):
    def __init__(self, username, email, password):
        super().__init__(username, password)
        self._email = email
        self._assigned_session = {}

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def assigned_session(self):
        return self._assigned_session

    def get_seminar_id(self, session_name):
        return int(self.assigned_session.get(session_name))

    def add_assigned_session(self, seminar, session):
        self.assigned_session[session.name] = seminar.id

    def is_admin(self):
        return False

    def is_guest(self):
        return True

    def __str__(self):
        return "name: {0}, email: {1}".format(self._username, self._email)

    def registerSeminar(self, seminar, session):
        if not self.avoid_speaker(session):
            return False
        elif super().registerSeminar(seminar, session) == False:
            return False

    #pass in a course
    def calculate_fee(self, event):
        currentDate = datetime.now().date()
        if event.fee < 0:
            return False

        if currentDate <= event.earlyRegDate:
            regFee = int(0.5*event.fee)
        else:
            regFee = event.fee

        return regFee
