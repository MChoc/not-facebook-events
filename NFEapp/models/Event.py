class Event:

    def __init__(self, status, date, time, location, maxAttendees, deRegWindow, abstractInfo):
        self._status = status
        self._date = date
        self._time = time
        self._location = _location
        self._attendeeList = []
        self._maxAttendees = maxAttendees
        self._deRegWindow = deRegWindow
        self._abstractInfo = abstractInfo

##
    def get_status(self):
        return self._status

    # TODO: add debugging
    # Email to be send when any setter is called?
    def set_status(self, status):
        self._status = status
##
##
    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date
##
##
    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time
##
##
    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location
##
##
    def get_attendeesList(self):
        return self._attendeeList

    def add_attendee(self, attendee):
        if attendee not in self._attendeeList:
            self._attendeeList.append(attendee)
            return 1
        else:
            return 0

    def remove_attendee(self, attendee):
        if attendee in self._attendeeList:
            self._attendeeList.remove(attendee)
            return 1
        else:
            return 0
##
##
    def get_maxAttendees(self):
        return self._maxAttendees

    def set_maxAttendees(self, maxAttendees):
        self._maxAttendees = maxAttendees
##
##
    def get_deRegWindow(self):
        return self._deRegWindow

    def set_deRegWindow(self, deRegWindow):
        self._deRegWindow = deRegWindow
##
##
    def get_abstractInfo(self):
        return self._abstractInfo

    def set_abstractInfo(self, abstractInfo):
        self._abstractInfo = abstractInfo
##
