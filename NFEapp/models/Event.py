class Event:

    def __init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo):
        self._name = name
        self._status = status
        self._date = date
        self._time = time
        self._location = location
        self._maxAttendees = maxAttendees
        self._deRegWindow = deRegWindow
        self._abstractInfo = abstractInfo
        self._attendeeList = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def status(self):
        return self._status

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
        return 0

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
    
    valid_statuses = ['open', 'closed', 'cancelled']
    @status.setter
    def status(self, status):
        if status not in valid_statuses:
            return 0
        else:
            self._status = status
            return 1
    
    def add_attendee(self, attendee):
        if attendee not in self._attendeeList:
            self._attendeeList.append(attendee)
            return 1
        else:
            return 0
        return 0
    
    def remove_attendee(self, attendee):
        if attendee in self._attendeeList:
            self._attendeeList.remove(attendee)
            return 1
        else:
            return 0
        return 0
    
    @property
    def attendeeList(self):
        return self._attendeeList