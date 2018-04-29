from Seminar import *
from Speaker import *

class Session:
    def __init__(self, name, date, time, location, maxAttendees, deRegWindow, abstractInfo, sessionStatus, speaker):
        self._name = name
        self._date = date
        self._time = time
        self._location = location
        self._maxAttendees = maxAttendees
        self._deRegWindow = deRegWindow
        self._abstractInfo = abstractInfo
        self._sessionStatus = sessionStatus       
        self._speaker = speaker
        self._type = "session"
        self._attendeeList = []

    def get_name(self):
	    return self._name

    def get_type(self):
	    return self._type
	
    def get_speaker(self):
        return self._speaker.get_name()

    def set_speaker(self, speaker):
        self._speaker = speaker
    
    def get_attendeeList(self):
        return self._attendeeList
	
    def add_attendee(self, member):
        self._attendeeList.append(member)
    
    def remove_attendee(self, member):
        self._attendeeList.remove(member)
    
    def get_sessionStatus(self):
        return self._sessionStatus
    
    def set_sessionStatus(self, status):
        self._sessionStatus = status
