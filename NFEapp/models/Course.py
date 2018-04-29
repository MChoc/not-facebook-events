from Event import *

class Course(Event):

    def __init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo):
        Event.__init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo)
        self._attendeeList = []
    
    @property
    def attendeeList(self):
        return self._attendeeList