from Seminar import *
from Speaker import *
from Event import *

class Session (Event):
    def __init__(self, name, date, time, location, maxAttendees, deRegWindow, abstractInfo, status, speaker):
        Event.__init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo)      
        self._speaker = speaker
        self._attendeeList = []

    @property
    def speaker(self):
        return self._speaker

    @speaker.setter
    def speaker(self, speaker):
        self._speaker = speaker
    
    @property
    def attendeeList(self):
        return self._attendeeList
	
    def add_attendee(self, member):
        self._attendeeList.append(member)
    
    def remove_attendee(self, member):
        self._attendeeList.remove(member)
    
