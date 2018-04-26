from UNSWMember import *

class Staff(UNSWMember):
    def __init__ (self, name, zID, email, password, role):
        super().__init__(name, zID, email, password, role)
        self._currentPostEvent = []
        self._pastPostEvent = []
        self._cancelledEvent = []
    
    def createEvent(self, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo, type,system):
        if type == 'course':
            event = Course(name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo, type)
        if type == 'seminar':
            event = Seminar(name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo, type)
            #have to add at least one session
        self._currentPostEvent.append(event)
        system.addOpenEvent(event)

    def get_current_post_event(self):
        return self._currentPostEvent
    
    def get_past_post_event(self):
        return self._pastPostEvent

    #change status of events, not sessions
    def changeStatus(self, event, status, system):
        event.set_status(status)
        self._currentPostEvent.remove(event)
        #don't worry about cancelling events now
        if status == "cancelled":
            self._cancelledEvent.append(event)
            system.removeOpenEvent(event)
        if status == "closed":
            self._pastPostEvent.append(event)
            system.removeOpenEvent(event)

    #pass in a course or a session
    def get_attendeeList(self, event):
        for attendee in event.get_attendeeList():
            print(attendee.__str__())
        