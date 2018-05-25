from .Event import *

class Course(Event):

    def __init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, fee, earlyRegDate, abstractInfo, presenter):
        Event.__init__(self, id, name, status, date, time, location, maxAttendees, deRegWindow, fee, earlyRegDate, abstractInfo)
        self._presenter = presenter

    @property
    def presenter(self):
        return self._presenter

    @presenter.setter
    def presenter(self, presenter):
        self._presenter = presenter