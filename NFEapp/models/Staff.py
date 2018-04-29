from UNSWMember import *

class Staff(UNSWMember):
    def __init__ (self, name, zID, email, password, role):
        UNSWMember.__init__(self, name, zID, email, password, role)
        self._currentPostEvent = []
        self._pastPostEvent = []
        self._cancelledEvent = []
    
    def createCourse(self, course, system):
        self._currentPostEvent.append(course)
        system.addOpenEvent(course)

    #assume type is seminar
    def createSeminar(self, seminar, session, system):
        for s in self._currentPostEvent:
            if s.get_name() == seminar.get_name():
                seminar.add_session(session)
                return True
        self._currentPostEvent.append(seminar)
        system.addOpenEvent(seminar)
        seminar.add_session(session)
        
    def get_current_post_event(self):
        return self._currentPostEvent
    
    def get_past_post_event(self):
        return self._pastPostEvent

    #change status of seminars or courses, not sessions
    def changeStatus(self, event, status, system):
        if self.avoid_creator(event) == True:
            return False
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
                #error happens there
                for e in attendee._currentEvents:
                    if e.get_name() == event.get_name():
                        attendee._currentEvents.remove(event)
                        attendee._pastEvents.append(event)
        elif event.get_type() == "seminar":
            for s in event.get_all_session():
                s.set_sessionStatus(status)
                for attendee in s.get_attendeeList():
                    for e in attendee._currentEvents:
                        if e.get_name() == event.get_name():
                            attendee._currentEvents.remove(event)
                            attendee._pastEvents.append(event)

    def change_session_status(self, seminar, session, status):
        if self.avoid_creator(seminar) == True:
            return False
        if seminar.get_status() == "closed":
            return False
        session.set_sessionStatus(status)


    #pass in a course or a session
    def get_attendeeList(self, event):
        if self.avoid_creator(event) == True:
            return False
        for attendee in event.get_attendeeList():
            print(attendee.__str__())
        
    #check that the event creator cannnot register for this event
    #check that person who want to get the attendee list is the creator
    def avoid_creator(self, event):
        for e in self._currentPostEvent:
            if event.get_name() == e.get_name():
                return False
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