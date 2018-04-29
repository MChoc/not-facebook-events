from datetime import datetime

class Event:

    def __init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo):
        self._name = name
        self._status = status
        self._date = date
        self._time = time
        self._location = _location
        self._attendeeList = []
        self._maxAttendees = maxAttendees
        self._deRegWindow = deRegWindow
        self._abstractInfo = abstractInfo


##
    @property
    def name(self):
        return name
    @name.setter
    def name(self):
##
    # returns str: "open", "closed" or "cancelled"
    @property
    def status(self):
        return self._status

    # TODO: add debugging
    # Email to be send when any setter is called?
    # arg1 str: "open", "closed" or "cancelled"
    # return int: 0 - failed (invalid status), 1 - success
    valid_statuses = ['open', 'closed', 'cancelled']
    @status.setter
    def status(self, status):
        if status not in valid_statuses:
            return 0
        else:
            self._status = status
            return 1
##
##
    # return: datetime.date
    @property
    def date(self):
        return self._date

    def valid_date(input_date):
        try:
            datetime.datetime.strptime(input_date, '%Y-%m-%d')
        except InputError:
            return 0
        return 1

    # arg1: date string in datetime format %Y-%m-%d
    # return int: 0 - failed (invalid date string), 1 - success
    @date.setter
    def date(self, date):
        if valid_date(date):
            self._date = date
            return 1
        else:
            return 0
##
##
    # return: datetime.time
    @property
    def time(self):
        return self._time

    def valid_time(input_time):
        try:
            datetime.datetime.strptime(input_time, '%H:%M')
        except InputError:
            return 0
        return 1

    # arg1: time string in datetime format %H:%M
    # return int: 0 - failed (invalid time string), 1 - success
    @time.setter
    def time(self, time):
        if valid_time(time):
            self._time = time
            return 1
        else:
            return 0
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
