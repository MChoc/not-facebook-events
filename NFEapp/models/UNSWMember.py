class UNSWMember:

    def __init__(self, name, zID, contact, password):
        self._name = name
        self._zID = zID
        self._contact = contact # TODO: DISCUSS list?
        self._password = password

    def get_name(self):
        return self._name

    def get_zID(self):
        return self._zID

    def get_contact(self):
        return self._contact

    def get_password(self):
        return self._password
