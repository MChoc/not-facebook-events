class EMS:
    def __init__(self):
        self._openEvent = []
        self._UNSWMemeber = []

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
