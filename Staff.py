class Staff(UNSWMember):

    def __init__(self, name, zID, contact, password, postHistory):
        UNSWMember.__init__(self, name, zId, contact, password)
        self._postHistory = postHistory[] # TODO: discuss as in events

    def get_name(self):
        return self._name

    def get_zID(self):
        return self._zID

    def get_contact(self):
        return self._contact

    def get_password(self):
        return self._password

    def get_postHistory(self):
        return self._postHistory[] # TODO discuss
