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

    def registerCourse(self, course):
        if self._avoid_closed_status(course) == False:
            return False

        if self._avoid_full(course) == False:
            return False

        if self._avoid_dup(course) == True:
            course.add_attendee(self)
            self.currentEvents.append(course)
            return True
        else:
            return False
    
    def _registerSession(self, session):
        session.add_attendee(self)

    def registerSeminar(self, seminar, session):
        if self._avoid_closed_status(seminar) == False:
            return False
        if session.status == "closed":
            return False

        if self._avoid_fake_session(seminar, session) != True:
            return False

        if self._avoid_full(session) == False:
            return False

        if self._avoid_dup(seminar) == True:
            self._registerSession(session)
            self.currentEvents.append(seminar)
            return True
        else:
            if self._avoid_dup_session(seminar, session) == True:
                self._registerSession(session)
                return True
            else:
                return False
    
    def _avoid_dup(self, event):
        if event in self.currentEvents:
            return False
        else:
            return True

    #check aganinst session history to avoid duplicated registration for sessions
    #return false if this person has registered for this session before
    def _avoid_dup_session(self, seminar, session):
        s = seminar.get_one_session(session.name)
        for user in s.attendeeList:
            if self.username == user.username:
                return False
        return True

    #check that the status of the event is not closed
    #return false if the event is already closed
    def _avoid_closed_status(self, event):
        if event.status == 'closed':
            return False

    #check that the session does belong to this seminar
    #return ture if the session belongs to this seminar
    def _avoid_fake_session(self, seminar, session):
        for s in seminar.session:
            if session.name == s.name:
                return True


    def _avoid_full(self, event):
        if len(event.attendeeList) >= event.maxAttendees:
            return False
    
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