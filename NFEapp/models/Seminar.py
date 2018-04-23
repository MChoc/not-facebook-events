class Seminar(Event):

    def __init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, session):
        Event.__init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo)
        self._session = session[]

    def get_session(self):
        return self._session # TODO:

    def add_session():
        return 0 # TODO: 
