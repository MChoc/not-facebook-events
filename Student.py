class Student(UNSWMember): # TODO discuss need for this class

    def __init__(self, name, zID, contact, password):
        UNSWMember.__init__(self, name, zID, contact, password)

    def get_name(self):
        return self._name

    def get_zID(self):
        return self._zID

    def get_contact(self):
        return self._contact

    def get_password(self):
        return self._password
