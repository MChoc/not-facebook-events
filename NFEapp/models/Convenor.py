from UNSWStaff import *
from Speaker import *
#for seminars

class Convenor(Staff):
    def __init__ (self, name, zID, email, password, role):
        super().__init__(name, zID, email, password, role)
    '''  
    def set_speaker(self, speaker, session):
        session.set_speaker(speaker)
    '''
    def create_session(status, date, time, location, maxAttendees, deRegWindow, abstractInfo, name, contact, seminar):
        speaker = Speaker(name, contact)
        session = Session(status, date, time, location, maxAttendees, deRegWindow, abstractInfo, speaker)
        seminar.add_session(session)
    
    def get_attendeeList(session):
        return session.get_attendeeList(session)
    
    def change_session_status(session, status):
        session.set_sessionStatus(status)
    
    def test():
        pass
