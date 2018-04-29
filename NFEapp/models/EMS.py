from UNSWMember import *
from Staff import *
from Student import *
from Convenor import *

class EMS:
    def __init__(self):
        self._openEvent = []
        self._UNSWMember = []

    def addOpenEvent(self, event):
        self._openEvent.append(event)
    
    def removeOpenEvent(self,event):
        self._openEvent.remove(event)
    
    def addUNSWMember(self, member):
        self._UNSWMember.append(member)
    
    def getUNSWMember(self, name):
        for person in self._UNSWMember:
            if person.name == name:
                return person
        return None
    
    def getOpenEvent(self, name):
        for event in self._openEvent:
            if event.name == name:
                return event
        return None
    
    def get_all_open_event(self):
        return self._openEvent