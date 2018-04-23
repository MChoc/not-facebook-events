class Staff(UNSWMember):

    def __init__(self, name, zID, contact, password, postHistory):
        UNSWMember.__init__(self, name, zId, contact, password)
        self._postHistory = postHistory[] # TODO: discuss as in events

    def postEvent():
        return 0 # TODO:

    def changeStatus():
        return 0 # TODO:

    def cancelEvent():
        return 0 # TODO:

    def get_postHistory(self):
        return self._postHistory[] # TODO discuss

    def get_attendeeList():
        return 0 # TODO:
