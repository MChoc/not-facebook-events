class Event:

    def __init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo, type):
        self._name = name
        self._status = status
        self._date = date
        self._time = time
        self._location = location
        self._maxAttendees = maxAttendees
        self._deRegWindow = deRegWindow
        self._abstractInfo = abstractInfo
        self._type = type
        self._attendeeList = []

    def get_name(self):
        return self._name

    def get_status(self):
        return self._status

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_location(self):
        return self._location

    def get_maxAttendees(self):
        return self._maxAttendees

    def get_deRegWindow(self):
        return self._deRegWindow

    def get_abstractInfo(self):
        return self._abstractInfo
        
    def get_type(self):
    	return self._type
    
    def set_status(self, status):
	    self._status = status
    
    def add_attendee(self, member):
        pass
    
    def remove_attendee(self, member):
        pass
    
    def get_attendeeList(self):
        pass