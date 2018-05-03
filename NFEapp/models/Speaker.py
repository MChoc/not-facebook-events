class Speaker:

    def __init__(self, name, contact):
        self._name = name
        self._contact = contact #email

    @property
    def name(self):
        return self._name

    @property
    def contact(self):
        return self._contact

    @name.setter
    def name(self, name):
        self._name = name

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    def __str__(self):
        return "Speaker name: {0}, contact: {1}".format(self._name, self._contact)
