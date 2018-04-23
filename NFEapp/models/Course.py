class Course(Event):

    def __init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo):
        Event.__init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo)
