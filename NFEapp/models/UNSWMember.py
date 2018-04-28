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

    #setters
    #do we need setters???
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

    def get_past_event(self):
        for event in self._currentEvents:
            if event.get_status == "closed":
                self._pastEvents.append(event)
                self._currentEvents.remove(event)
        return self._pastEvents
        
    def get_current_session(self, seminar):
        current_session = []
        for event in self._currentEvents:
            if seminar.get_name() == event.get_name():
                for session in event.get_all_session():
                    for attendee in session.get_attendeeList():
                        if self._name == attendee.name:
                            current_session.append(session)
        return current_session
    
    #register for courses
    def registerCourse(self, course):
        if self.avoid_closed_status(course) == False:
            return False
        if self.avoid_dup(course) == True:
            course.add_attendee(self)
            self._currentEvents.append(course)
        else:
            return False

    def registerSession(self, session):
        session.add_attendee(self)

    def registerSeminar(self, seminar, session):
        if self.avoid_closed_status(seminar) == False:
            return False
        if session.get_sessionStatus() == "closed":
            return False
        
        if self.avoid_dup(seminar) == True:
            self.registerSession(session)
            self._currentEvents.append(seminar)
        else:
            if self.avoid_dup_session(seminar, session) == True:
                self.registerSession(session)
            else:
                return False

    #check against registration history to avoid duplicated registeration for events
    def avoid_dup(self, event):
        for e in self._currentEvents:
            if event.get_name() == e.get_name():
                return False
        return True 

    #check aganinst session history to avoid duplicated registration for sessions 
    def avoid_dup_session(self, seminar, session):
        s = seminar.get_one_session(session.get_name())
        for user in s.get_attendeeList():
            if self._name == user.name:
                return False
        return True

    def avoid_closed_status(self, event):
        if event.get_status() == 'closed':
            return False


    #deregister from courses and sessions
    def deRegister(self, event):
        if event.get_type() == "course":
            self._currentEvents.remove(event)
            event.remove_attendee(self)
        elif event.get_type() == "seminar":
            #deregister from every sessions
            for session in event.get_all_session():
                for attendee in session.get_attendeeList():
                    if self._name == attendee.name:
                        session.remove_attendee(self)
                        break
            self._currentEvents.remove(event)

        #if the session deregistered is the only session registered in a seminar before,
        #then deregistering this session will remove this seminar from the current event list
        #if not, deregistering will only remove the session, not the whole seminar 
    
    def deRegisterSession(self, seminar, session):
        session.remove_attendee(self)
        flag = 0
        for session in seminar.get_all_session():
            for attendee in session.get_attendeeList():
                if self._name == attendee.name:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            self._currentEvents.remove(seminar)
