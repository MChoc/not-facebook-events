#from abc import ABC, abstractmethod
from Event import *
from Course import *
from Seminar import *
from datetime import datetime

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
    
    @property
    def currentEvents(self):
        return self._currentEvents

    @property
    def pastEvents(self):
        return self._pastEvents
        
    #return current sessions that the user registered for in a seminar
    #pass in a seminar object
    #need to check that this user has registered for this seminar before
    #return false if not successful
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
    #pass in a course that the user intends to register for
    #need to check that the status of the course is not closed
    #need to check that this user has not registered for this course before
    #return false is not successful
    def registerCourse(self, course):
        if self.avoid_closed_status(course) == False:
            return False
        if self.avoid_dup(course) == True:
            course.add_attendee(self)
            self._currentEvents.append(course)
            return True
        else:
            return False

    #pass in a session that the user intends to register for
    #used inside registerSeminar method, not for individual use
    def registerSession(self, session):
        session.add_attendee(self)

    #register for seminar
    #pass in a seminar and a session of the seminar that the user intends to register for
    #need to check that status of the seminar and the session is not closed
    #need to check that this session belongs to this semianr
    #return false if unsuccessful
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
    #return false if the person has registerer for this event before
    #return true if the person has not registered before
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
    #return false if this person has registered for this session before
    def avoid_dup_session(self, seminar, session):
        s = seminar.get_one_session(session.name)
        for user in s.attendeeList:
            if self.name == user.name:
                return False
        return True

    #check that the status of the event is not closed
    #return false if the event is already closed
    def avoid_closed_status(self, event):
        if event.status == 'closed':
            return False

    #check that the session does belong to this seminar
    #return ture if the session belongs to this seminar
    def avoid_fake_session(self, seminar, session):
        for s in seminar.sessions:
            if session.name == s.name:
                return True

    #deregister for course
    #pass in a course that the user intends to deregister for
    #need to check that this user has registered for this course before
    #need to check time that allow for deregister is not passed
    def deRegisterCourse(self, course):
        if self.check_time_validation(course.deRegWindow) == False:
            return False
        if self.check_registration(course) != True:
            return False
        
        self._currentEvents.remove(course)
        course.remove_attendee(self)

    #deregister for semianr
    #pass in a semianr that the user intends to deregister for
    #thus deregister from all sessions in the seminar
    #need to check that this user has registered for this seminar before
    ##need to check time that allow for deregister is not passed
    def deRegisterSeminar(self, seminar):
        #if self.check_time_validation(course.deRegWindow) == False:
        #    return False
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
    #need to check that this user has registered for this seminar before
    #need to check that this session belongs to this seminar
    #need to check time that allow for deregister is not passed
    def deRegisterSession(self, seminar, session):
        if self.check_registration(seminar) != True:
            return False
        if self.avoid_fake_session(seminar, session) != True:
            return False
        if self.check_time_validation(session.deRegWindow) == False:
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
    #return true if this event has been registered for before
    def check_registration(self, event):
        for e in self._currentEvents:
            if e.name == event.name:
                return True
    
    #compare current time and deregDate
    #check that deregister is allowed
    #return true if time is valid(deregister is allowed)
    def check_time_validation(self, deRegDate):
        deRegDate = datetime.strptime(deRegDate, '%Y-%m-%d')
        currentDate = datetime.now()
        if currentDate > deRegDate:
            print("time passed")
            return False
        else:
            return True