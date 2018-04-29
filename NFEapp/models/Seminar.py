from Session import *
from Event import *
class Seminar(Event):

    def __init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo):
        Event.__init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo)
        self._session = []

    # return list[session]
    @property
    def sessions(self):
        return self._session

    # adds session to session list in Seminar
    # arg1 session
    def add_session(self, session):
        self._session.append(session)
    
    def get_one_session(self, name):
        for session in self._session:
            if session.name == name:
                return session
        return None

