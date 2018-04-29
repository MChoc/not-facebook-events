from Seminar import *
from Speaker import *
from Event import *

class Session (Event):
    def __init__(self, name, date, time, location, maxAttendees, deRegWindow, abstractInfo, status, speaker):
        Event.__init__(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo)      
        self._speaker = speaker

    @property
    def speaker(self):
        return self._speaker

    @speaker.setter
    def speaker(self, speaker):
        self._speaker = speaker
    
    
