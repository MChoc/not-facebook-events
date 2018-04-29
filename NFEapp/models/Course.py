from Event import *

class Course(Event):

    def __init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo, type):
        Event.__init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo, type)
    
    def add_attendee(self, member):
    	self._attendeeList.append(member)
    
    def remove_attendee(self, member):
    	self._attendeeList.remove(member)
    
    def get_attendeeList(self):
	    return self._attendeeList