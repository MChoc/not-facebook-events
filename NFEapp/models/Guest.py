from .Member import *
from .Course import *
from .Seminar import *
from datetime import datetime

class Guest(Member):
    def __init__(self, username, email, password):
        super().__init__(username, password)
        self._email = email
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def is_admin(self):
        return False

    def is_guest(self):
        return True

    def __str__(self):
        return "name: {0}, email {1}".format(self._username, self._email)

    def registerSeminar(self, seminar, session):
        if not self.avoid_speaker(session):
            return False
        else:
            super().registerSeminar(seminar, session)
    
    #when register, need to check that the person is not the speaker
    def avoid_speaker(self, session):
        if session.speaker.get_id() == self.get_id():
            return False
        else:
            return True
    
    def calculate_fee(self, event):
        currentDate = datetime.now().date()
        
        if currentDate < event.earlyRegDate:
            regFee = 0.5*event.fee
        else:
            regFee = event.fee
            
        if isinstance(event, Session):
            if not self.avoid_speaker(event):
                regFee = 0
        
        return regFee