from .UNSWMember import *

class Staff(UNSWMember):
    def __init__ (self, username, zID, email, password, role):
        UNSWMember.__init__(self, username, zID, email, password, role)
        self._currentPostEvent = []
        self._pastPostEvent = []
        self._cancelledEvent = []

    @property
    def currentPostEvent(self):
        return self._currentPostEvent

    @property
    def pastPostEvent(self):
        return self._pastPostEvent

    @property
    def cancelledEvent(self):
        return self._cancelledEvent

    #create a new course
    def createCourse(self, course):
        self.currentPostEvent.append(course)

    '''
    #create a new seminar or a new sesssion in the semianr
    def createSeminar(self, seminar, session):
        for s in self._currentPostEvent:
            if s.name == seminar.name:
                seminar.add_session(session)
                return True
        self._currentPostEvent.append(seminar)
        seminar.add_session(session)
    '''

    def createSeminar(self, seminar, session):
        self.currentPostEvent.append(seminar)
        seminar.add_session(session)

    def addSession(self, seminar, session):
        for s in self.currentPostEvent:
            if s.name == seminar.name:
                seminar.add_session(session)
                return True

    #change status of seminars or courses, not sessions
    #used for changeCourseStatus or changeSeminarStatus, not for individual use
    def changeStatus(self, event, status):
        if self.avoid_creator(event) == True:
            return False
        self.currentPostEvent.remove(event)
        event.status = status
    
        #don't worry about cancelling events now
        if status == "cancelled":
            self.cancelledEvent.append(event)
        if status == "closed":
            print("closing")
            self.pastPostEvent.append(event)
        
        
        print(self.pastPostEvent)

    #change the status of a course
    #need to check that the person who wants to change the status
        #must be person who create this course
    def changeCourseStatus(self, course, status):
        if self.changeStatus(course, status) == False:
            return False
        for attendee in course.attendeeList:
            for e in attendee._currentEvents:
                if e.name == course.name:
                    attendee.currentEvents.remove(course)
                    attendee.pastEvents.append(course)

    #change the status of a seminar
    #need to check that the person who wants to change the status
        #must be person who create this seminar
    #change the status of the seminar will sequentially change
        #status of all sessions in the seminar
    def changeSeminarStatus(self, seminar, status):
        if self.changeStatus(seminar, status) == False:
            return False
        for s in seminar.session:
            s.status = status
            for attendee in s.attendeeList:
                for e in attendee.currentEvents:
                    if e.name == seminar.name:
                        attendee.currentEvents.remove(seminar)
                        attendee.pastEvents.append(seminar)

    #change status of a session
    #need to check that the person who wants to change the status
        #must the person who create the seminar
    #return false if unsuccessful
    #return false if the session has already closed
    def changeSessionStatus(self, seminar, session, status):
        if self.avoid_creator(seminar) == True:
            return False
        if self._avoid_fake_session(seminar, session) != True:
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

    # NEW 3.5.18
    def is_admin(self):
        return True
