from UNSWMember import *

class Staff(UNSWMember):
    def __init__ (self, name, zID, email, password, role):
        UNSWMember.__init__(self, name, zID, email, password, role)
        self._currentPostEvent = []
        self._pastPostEvent = []
        self._cancelledEvent = []
    
    @property
    def currentPostEvent(self):
        return self._currentPostEvent
    
    @property
    def pastPostEvent(self):
        return self._pastPostEvent
    
    #create a new course
    def createCourse(self, course, system):
        self._currentPostEvent.append(course)
        system.addOpenEvent(course)

    #create a new seminar or a new sesssion in the semianr
    def createSeminar(self, seminar, session, system):
        for s in self._currentPostEvent:
            if s.name == seminar.name:
                seminar.add_session(session)
                return True
        self._currentPostEvent.append(seminar)
        system.addOpenEvent(seminar)
        seminar.add_session(session)
        
    
    #change status of seminars or courses, not sessions
    #used for changeCourseStatus or changeSeminarStatus, not for individual use
    def changeStatus(self, event, status, system):
        if self.avoid_creator(event) == True:
            return False
        event.status = status
        self._currentPostEvent.remove(event)
        #don't worry about cancelling events now
        if status == "cancelled":
            self._cancelledEvent.append(event)
            system.removeOpenEvent(event)
        if status == "closed":
            self._pastPostEvent.append(event)
            system.removeOpenEvent(event)

    #change the status of a course
    #need to check that the person who wants to change the status
        #must be person who create this course
    def changeCourseStatus(self, course, status, system):
        self.changeStatus(course, status, system)
        for attendee in course.attendeeList:
            for e in attendee._currentEvents:
                if e.name == course.name:
                    attendee._currentEvents.remove(course)
                    attendee._pastEvents.append(course)
    
    #change the status of a seminar
    #need to check that the person who wants to change the status
        #must be person who create this seminar
    #change the status of the seminar will sequentially change
        #status of all sessions in the seminar
    def changeSeminarStatus(self, seminar, status, system):
        self.changeStatus(seminar, status, system)
        for s in seminar.sessions:
            s.status = status
            for attendee in s.attendeeList:
                for e in attendee.currentEvents:
                    if e.name == seminar.name:
                        attendee._currentEvents.remove(seminar)
                        attendee._pastEvents.append(seminar)
    
    #change status of a session
    #need to check that the person who wants to change the status
        #must the person who create the seminar
    #return false if unsuccessful
    #return false if the session has already closed
    def change_session_status(self, seminar, session, status):
        if self.avoid_creator(seminar) == True:
            return False
        if self.avoid_fake_session(seminar, session) != True:
            return False
        if seminar.status == "closed":
            return False
        session.status = status
    
    #check that the event creator cannnot register for this event
    #check that person who want to get the attendee list is the creator
    #if the person is not the event creator, will return true
    #if the person is the creator, will return false
    #logic is suggested by the name, if not creator, thus succesfully avoid creator and return true
    def avoid_creator(self, event):
        flag = 0
        for e in self.currentPostEvent:
            if event.name == e.name:
                flag = 1
                break
        #not the creator will return true
        if flag == 0:
            return True
        elif flag == 1:     
            return False

    #staff register course
    #inherited from UNSWMember
    #need to check that the staff who wants to registers for this course
        #is not the one who created it
    def registerCourse(self, event):
        if self.avoid_creator(event) == True:
            if super().registerCourse(event) == False: 
                return False
        else:
            return False
    
    #staff register seminar
    #inherited from UNSWMember
    #need to check that the staff who wants to registers for this seminar
        #is not the one who created it
    def registerSeminar(self, seminar, session):
        if self.avoid_creator(seminar) == True:
            if UNSWMember.registerSeminar(self, seminar, session) == True:
                return True
        else:
            return False