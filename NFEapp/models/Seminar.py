from Event import *

# attendeeList for Seminar should be None
class Seminar(Event):

    def __init__(self, id, name, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo):
        Event.__init__(self, id, name, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo)
        self._date = None
        self._time = None
        self._location = None
        self._maxAttendees = None
        self._deRegWindow = None
        self._session = []
        # special case: self._attendeeList = list[list[UNSWMember]]


##
    # return list[session]
    @property
    def sessions(self):
        return self._session

    # adds session to session list in Seminar
    # arg1 session
    def add_session(self, session):
        self._session.append(session)
##
