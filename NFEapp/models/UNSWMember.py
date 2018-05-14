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


    #deregister for course
    #pass in a course that the user intends to deregister for
    #need to check that this user has registered for this course before
    #need to check time that allow for deregister is not passed
    def deRegisterCourse(self, course):
        if self._check_time_validation(course.deRegWindow) == False:
            return False
        if self._avoid_dup(course) == True:
            return False

        self.currentEvents.remove(course)
        course.remove_attendee(self)

    #deregister for semianr
    #pass in a semianr that the user intends to deregister for
    #thus deregister from all sessions in the seminar
    #need to check that this user has registered for this seminar before
    def deRegisterSeminar(self, seminar):
        if self._avoid_dup(seminar) == True:
            return False

        #deregister from every sessions
        for session in seminar.session:
            for attendee in session.attendeeList:
                if self.username == attendee.username:
                    session.remove_attendee(self)
                    break
        self.currentEvents.remove(seminar)

    #if the session deregistered is the only session registered in a seminar before,
    #then deregistering this session will remove this seminar from the current event list
    #if not, deregistering will only remove the session, not the whole seminar
    #need to check that this user has registered for this seminar before
    #need to check that this session belongs to this seminar
    #need to check time that allow for deregister is not passed
    def deRegisterSession(self, seminar, session):
        if self._avoid_dup(seminar) == True:
            return False
        if self._avoid_fake_session(seminar, session) != True:
            return False
        if self._check_time_validation(session.deRegWindow) == False:
            return False

        if self in session.attendeeList:
            session.remove_attendee(self)

        flag = 0
        for session in seminar.session:
            if self in session.attendeeList:
                flag=1
                break

        if flag == 0:
            self.currentEvents.remove(seminar)

    #used for deRegistration
    #check that intended deregistered event is registered before
    def _check_registration(self, event):
        for e in self.currentEvents:
            if e.name == event.name:
                return True


    #compare current time and deregDate
    #check that deregister is allowed
    #return true if time is valid(deregister is allowed)
    def _check_time_validation(self, deRegDate):
        currentDate = datetime.now().date()
        if currentDate > deRegDate:
            return False
        else:
            return True
