class Seminar(Event):

    def __init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, session):
        Event.__init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo)
        self._session = []

    def get_session(self):
        return self._session

    def add_session(self, session):
        self._session.append(session)
