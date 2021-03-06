from flask_login import UserMixin
from abc import ABC, abstractmethod
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Member(UserMixin, ABC):
    __id = -1

    @abstractmethod
    def __init__(self, username, password):
        self._id = self._generate_id()
        self._username = username
        self._password = generate_password_hash(password)

        self._currentEvents = []
        self._pastEvents = []

    @property
    def username(self):
        return self._username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def id(self):
        return self._id

    def get_id(self):
        return str(self._id)

    def _generate_id(self):
        Member.__id += 1
        return Member.__id

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @abstractmethod
    def is_admin(self):
        pass

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
        if self._avoid_dup(seminar) == True:
            return False

        current_session = []
        for session in seminar.session:
            if session.status == 'open':
                if self in session.attendeeList:
                    current_session.append(session)
        return current_session

    #check against registration history to avoid duplicated registeration for events
    #return false if the person has registerer for this event before
    #return true if the person has not registered before
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

    #register for courses
    #pass in a course that the user intends to register for
    #need to check that the status of the course is not closed
    #need to check that this course is not full
    #need to check that this user has not registered for this course before
    #return false is not successful
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

    #pass in a session that the user intends to register for
    #used inside registerSeminar method, not for individual use
    def _registerSession(self, session):
        session.add_attendee(self)

    #register for seminar
    #pass in a seminar and a session of the seminar that the user intends to register for
    #need to check that status of the seminar and the session is not closed
    #need to check that this session belongs to this semianr
    #need to check that this session is not full
    #return false if unsuccessful
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
    #need to check that dereg date for seminar is not expired
    def deRegisterSeminar(self, seminar):
        if self._avoid_dup(seminar) == True:
            return False

        if self.valid_seminar_dereg_date(seminar) == False:
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

    #check allowed date for deregistering a seminar
    #return earlist allowable deregister date for a seminar
    #this date should be the earlist dereg date
    #among current enrolled sessions in this seminar
    def valid_seminar_dereg_date(self, seminar):
        earlist_date = datetime.strptime('2999-01-01', '%Y-%m-%d').date()
        for session in self.get_current_session(seminar):
            if session.deRegWindow < earlist_date:
                earlist_date = session.deRegWindow

        return self._check_time_validation(earlist_date)

    #when register, need to check that the person is not the speaker
    def avoid_speaker(self, session):
        if session.speaker.email == self.email:
            return False
        else:
            return True
