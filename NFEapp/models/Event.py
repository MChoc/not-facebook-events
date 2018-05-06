from datetime import datetime
from abc import ABC, abstractmethod

class Event(ABC):

    @abstractmethod
    def __init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo):
        self._id = id
        self._name = name
        self._status = status
        self._date = self._conform_date_format(date)
        self._time = self._conform_time_format(time)
        self._location = location
        self._maxAttendees = maxAttendees
        self._deRegWindow = self._conform_date_format(deRegWindow)
        self._abstractInfo = abstractInfo
        self._attendeeList = []


##
    # prints out information about the event
    def __str__(self):
        return "{}".format(self._name)
##
    # Do not allow users to change the id of events
    # handled by the system
    @property
    def id(self):
        return self._id
##
##
    # return str: name of event
    @property
    def name(self):
        return self._name

    # sets/changes name of event
    # arg1 str: name to change to
    @name.setter
    def name(self, name):
        self._name = name
##
##
    # return str: "open", "closed" or "cancelled"
    @property
    def status(self):
        return self._status

    # Email to be send when any setter is called?
    # arg1 str: "open", "closed" or "cancelled"
    # return int: 0 - failed (invalid status), 1 - success
    @status.setter
    def status(self, status):
        valid_statuses = ['open', 'closed', 'cancelled']
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

    def _valid_date(input_date):
        try:
            datetime.strptime(input_date, '%Y-%m-%d').date()
        except ValueError:
            return 0
        return 1

    # arg1: date string in datetime format %Y-%m-%d
    # return int: 0 - failed (invalid date string), 1 - success
    @date.setter
    def date(self, date):
        if _valid_date(date):
            self._date = date
            return 1
        else:
            return 0
##
##
    #conform date format as date
    def _conform_date_format(self, date):
        if isinstance(date, str):
            return datetime.strptime(date, '%Y-%m-%d').date()
        else:
            return date
##
##   
    # return: datetime.time
    @property
    def time(self):
        return self._time

    def _valid_time(input_time):
        try:
            datetime.strptime(input_time, '%H:%M').time()
        except ValueError:
            return 0
        return 1

    # arg1: time string in datetime format %H:%M
    # return int: 0 - failed (invalid time string), 1 - success
    @time.setter
    def time(self, time):
        if _valid_time(time):
            self._time = time
            return 1
        else:
            return 0
        return 0
##
##
    def _conform_time_format(self, time):
        if isinstance(time, str):
            time = datetime.strptime(time, '%H:%M')
            return time.strftime("%H:%M")
        else:
            return time.strftime("%H:%M")

    # return str: location of event
    @property
    def location(self):
        return self._location

    # arg1 str: location of event
    @location.setter
    def location(self, location):
        self._location = location

    @property
    def maxAttendees(self):
        return self._maxAttendees

    # sets max number of attendees for an event
    # arg1 int
    # return int: 0 - failed, 1 - success
    @maxAttendees.setter
    def maxAttendees(self, maxAttendees):
        if maxAttendees < 0:
            return 0
        else:
            self._maxAttendees = maxAttendees
            return 1
        return 0

    @property
    def deRegWindow(self):
        return self._deRegWindow

    # sets deRegistration window
    # arg1 int
    @deRegWindow.setter
    def deRegWindow(self, deRegWindow):
        self._deRegWindow = deRegWindow
##
##
    # return list[UNSWMember]
    @property
    def attendeeList(self):
        return self._attendeeList

    # appends a UNSWMember onto attendeeList
    # arg1 UNSWMember
    # return int: 0 - failed, 1 - success
    def add_attendee(self, attendee):
        if attendee not in self._attendeeList:
            self._attendeeList.append(attendee)
            return 1
        else:
            return 0
        return 0

    # removes specified attendee from attendeeList
    # arg1 UNSWMember
    # return int: 0 - failed, 1 - success
    def remove_attendee(self, attendee):
        if attendee in self._attendeeList:
            self._attendeeList.remove(attendee)
            return 1
        else:
            return 0
        return 0
##
##
    # return int: maxAttendees
    @property
    def maxAttendees(self):
        return self._maxAttendees

    # sets max number of attendees for an event
    # arg1 int
    # return int: 0 - failed, 1 - success
    @maxAttendees.setter
    def maxAttendees(self, maxAttendees):
        if maxAttendees < 0:
            return 0
        else:
            self._maxAttendees = maxAttendees
            return 1
        return 0
##
##
    # return int: deRegWindow
    @property
    def deRegWindow(self):
        return self._deRegWindow

    # sets deRegistration window
    # arg1 int
    @deRegWindow.setter
    def deRegWindow(self, deRegWindow):
        self._deRegWindow = deRegWindow
##
##
    # return str: Information of event
    @property
    def abstractInfo(self):
        return self._abstractInfo

    # sets information for event
    # arg1 str: event information
    # return int: 0 - failed, 1 - success
    @abstractInfo.setter
    def abstractInfo(self, abstractInfo):
        self._abstractInfo = abstractInfo
##
