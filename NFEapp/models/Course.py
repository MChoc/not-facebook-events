class Course(Event):

    def __init__(self, id, name, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo):
        Event.__init__(self, id, name, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo)
