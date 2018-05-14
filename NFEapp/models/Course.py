from .Event import *

class Course(Event):

    def __init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, fee, earlyRegDate, abstractInfo):
        Event.__init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, fee, earlyRegDate, abstractInfo)
