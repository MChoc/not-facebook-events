from Session import *
from Event import *
class Seminar(Event):

    def __init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo):
        Event.__init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo)
        self._session = []
        self._attendeeList = []

    def add_session(self, session):
        self._session.append(session)
    
    def get_all_session(self):
        return self._session
    
    def get_one_session(self, name):
        for session in self._session:
            if session.name == name:
                return session
        return None
    
    #attendeelist for seminar is a list of list
    def get_attendee(self):
        for session in self._session:
            self._attendeeList.append(session.get_attendeeList())
        return self._attendeeList
