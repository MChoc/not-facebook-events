from .UNSWMember import *
from .Event import *
from .Course import *
from .Seminar import *
from .Staff import *
from .Student import *
from .Speaker import *
from .Session import *
from .Member import *

class EMS:
    __id = -1  #course/event id
    __sid = -1 #session id

    def __init__(self):
        self._openEvent = []
        self._UNSWMember = []

    @property
    def openEvent(self):
        return self._openEvent

    @property
    def UNSWMember(self):
        return self._UNSWMember

    def _generate_id(self):
        EMS.__id += 1
        return EMS.__id

    def _generate_sid(self):
        EMS.__sid += 1
        return EMS.__sid

    def addOpenEvent(self, event):
        self.openEvent.append(event)

    def removeOpenEvent(self,event):
        self.openEvent.remove(event)

    #search open events
    #pass in key words
    #return a list of events whose name contains that key words
    def search_open_events(self, name):
        current_list = []
        for event in self.openEvent:
            if name in event.name:
                current_list.append(event)
        return current_list

    def addUNSWMember(self, member):
        self.UNSWMember.append(member)

    def getUNSWMember(self, username):
        for person in self.UNSWMember:
            if person.username == username:
                return person
        return None

    def getOpenEvent(self, name):
        for event in self.openEvent:
            if event.name == name:
                return event
        return None

    def create_open_course(self, user, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo):
        id = self._generate_id()
        course = Course(id, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo)
        user.createCourse(course)
        self.addOpenEvent(course)

    def create_open_seminar(self, user, name, status, abstractInfo, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sabstractInfo, sspeaker):
        id = self._generate_id()
        sid = self._generate_sid()
        seminar = Seminar(id, name, status, abstractInfo)
        session = Session(sid, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sabstractInfo, sspeaker)
        user.createSeminar(seminar, session)
        self.addOpenEvent(seminar)

    def add_session(self, user, seminar, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sabstractInfo, sspeaker):
        if user.avoid_creator(seminar) == True:
            return False

        sid = self._generate_sid()
        session = Session(sid, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sabstractInfo, sspeaker)
        user.addSession(seminar, session)

    def change_course_status(self, user, course, status):
        if user.changeCourseStatus(course, status) == False:
            return False
        self.removeOpenEvent(course)

    def change_seminar_status(self, user, seminar, status):
        if user.changeSeminarStatus(seminar, status) == False:
            return False
        self.removeOpenEvent(seminar)

    def change_session_status(self, user, seminar, session, status):
        if user.changeSessionStatus(seminar, session, status) == False:
            return False

    def register_course(self, user, course):
        if user.registerCourse(course) == False:
            return False

    def register_seminar(self, user, seminar, session):
        if user.registerSeminar(seminar, session) == False:
            return False

    def deRegister_course(self, user, course):
        if user.deRegisterCourse(course) == False:
            return False

    def deRegister_seminar(self, user, seminar):
        if user.deRegisterSeminar(seminar) == False:
            return False

    def deRegister_session(self, user, seminar, session):
        if user.deRegisterSession(seminar, session) == False:
            return False

    def get_current_session(self, user, seminar):
        if user.get_current_session(seminar) == False:
            return False
        return user.get_current_session(seminar)

    def validate_login(self, username, password):
        for c in self.UNSWMember:
            if c.username == username and c.check_password(password):
                return c
        return None

    def get_user_by_id(self, user_id):
        for c in self.UNSWMember:
            if c.get_id() == user_id:
                return c
        return None
