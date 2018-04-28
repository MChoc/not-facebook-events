from UNSWMember import *

class Staff(UNSWMember):
    def __init__ (self, name, zID, email, password, role):
        UNSWMember.__init__(self, name, zID, email, password, role)
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

        if event.get_type() == "course":
            for attendee in event.get_attendeeList():
                attendee._currentEvents.remove(event)
                attendee._pastEvents.append(event)
        elif event.get_type() == "seminar":
            for s in event.get_all_session():
                s.set_sessionStatus(status)
                for attendee in s.get_attendeeList():
                    for event in attendee._currentEvents:
                        attendee._currentEvents.remove(event)
                        attendee._pastEvents.append(event)

    def change_session_status(self, seminar, session, status):
        if seminar.get_status() == "closed":
            return False
        session.set_sessionStatus(status)


    #pass in a course or a session
    def get_attendeeList(self, event):
        for attendee in event.get_attendeeList():
            print(attendee.__str__())
        
    #check that the event creator cannnot register for this event
    def avoid_creator(self, event):
        for e in self._currentPostEvent:
            if event.get_name() == e.get_name():
                return False
        else:
            return True
    
    def registerCourse(self, event):
        if self.avoid_creator(event) == True:
            if super().registerCourse(event) == False: 
                return False
        else:
            return False
    
    def registerSeminar(self, seminar, session):
        if self.avoid_creator(seminar) == True:
            if UNSWMember.registerSeminar(self, seminar, session) == True:
                return True
        else:
            return False