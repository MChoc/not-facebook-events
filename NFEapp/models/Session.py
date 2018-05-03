from .Seminar import *
from .Speaker import *
from .Event import *


class Session(Event):

    def __init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo, speaker):
        Event.__init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo)
        self._speaker = speaker

##
    # return str: speaker for session
    @property
    def speaker(self):
        return self._speaker

    # changes speaker
    # arg1 Speaker
    @speaker.setter
    def speaker(self, speaker):
        self._speaker = speaker
##
