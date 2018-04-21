class Seminar(Event):

    def __init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, session):
        Event.__init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo)
        self._session = session[]

    def get_status(self):
        return self._status

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_location(self):
        return self._location

    # TODO: INCOMPLETE
    def get_attendeesList(self):
        return self._attendeeList

    def get_maxAttendees(self):
        return self._maxAttendees

    def get_deRegWindow(self):
        return self._deRegWindow

    def get_abstractInfo(self):
        return self._abstractInfo

    def get_session(self):
        return self._session
