#from abc import ABC, abstractmethod
from Event import *
from Course import *
from Seminar import *


class UNSWMember(object):

    def __init__ (self, name, zID, email, password, role):
        self._name = name
        self._zID = zID
        self._email = email
        self._password = password
        self._role = role
        self._currentEvents = []
        self._pastEvents = []

    #getters
    @property
    def name(self):
        return self._name

    @property
    def zID(self):
        return self._zID

    @property
    def email(self):
        return self._email

    @property
    def role(self):
        return self._role

    @name.setter
    def name(self, name):
        self._name = name

    @email.setter
    def email(self, email):
        self._email = email

    @role.setter
    def role(self, role):
        self._role = role

    def validate_password(self, password):
        return self._password == password

    def __str__(self):
        return "Attdenee detail: \nname: {0}, email: {1}".format(self._name, self._email)

    def get_current_event(self):
        return self._currentEvents

    #need to test
    @property
    def pastEvents(self):
        return self._pastEvents
    def get_current_session(self, seminar):
        if self.avoid_dup(seminar) == True:
            return False       
        
        current_session = []
        for session in seminar.sessions:
            for attendee in session.attendeeList:
                if self.name == attendee.name:
                    current_session.append(session)
        return current_session

    #register for courses
    def registerCourse(self, course):
        if self.avoid_closed_status(course) == False:
            return False
        if self.avoid_dup(course) == True:
            course.add_attendee(self)
            self._currentEvents.append(course)
            return True
        else:
            return False

    def registerSession(self, session):
        session.add_attendee(self)

    def registerSeminar(self, seminar, session):
        if self.avoid_closed_status(seminar) == False:
            return False
        if session.status == "closed":
            return False
        
        if self.avoid_fake_session(seminar, session) != True:
            return False

        if self.avoid_dup(seminar) == True:
            self.registerSession(session)
            self._currentEvents.append(seminar)
            return True
        else:
            if self.avoid_dup_session(seminar, session) == True:
                self.registerSession(session)
                return True
            else:
                return False

    #check against registration history to avoid duplicated registeration for events
    def avoid_dup(self, event):
        flag = 0
        for e in self.currentEvents:
            if event.name == e.name:
                flag = 1
                break
        if flag == 1:
            return False
        else:
            return True 

    #check aganinst session history to avoid duplicated registration for sessions 
    def avoid_dup_session(self, seminar, session):
        s = seminar.get_one_session(session.name)
        for user in s.attendeeList:
            if self.name == user.name:
                return False
        return True

    def avoid_closed_status(self, event):
        if event.status == 'closed':
            return False

    def avoid_fake_session(self, seminar, session):
        for s in seminar.sessions:
            if session.name == s.name:
                return True

    def deRegisterCourse(self, course):
        if self.check_registration(course) != True:
            return False
        
        self._currentEvents.remove(course)
        course.remove_attendee(self)

    def deRegisterSeminar(self, seminar):
        if self.check_registration(seminar) != True:
            return False
        
        #deregister from every sessions
        for session in seminar.sessions:
            for attendee in session.attendeeList:
                if self.name == attendee.name:
                    session.remove_attendee(self)
                    break
        self._currentEvents.remove(seminar)

    #if the session deregistered is the only session registered in a seminar before,
    #then deregistering this session will remove this seminar from the current event list
    #if not, deregistering will only remove the session, not the whole seminar 
    
    def deRegisterSession(self, seminar, session):
        if self.check_registration(seminar) != True:
            return False
        for attendee in session.attendeeList:
            if self.name == attendee.name:
                session.remove_attendee(self)
                flag = 0
                for session in seminar.sessions:
                    for attendee in session.attendeeList:
                        if self.name == attendee.name:
                            flag = 1
                            break
                    if flag == 1:
                        break
                if flag == 0:
                    self._currentEvents.remove(seminar)
                break
            else:
                return False
    
    #used for deRegistration
    #check that intended deregistered event is registered before
    def check_registration(self, event):
        for e in self._currentEvents:
            if e.name == event.name:
                return True