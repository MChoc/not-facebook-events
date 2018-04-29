class Speaker(object):

    def __init__(self, name, contact):
        self._name = name
        self._contact = contact #email

    def get_name(self):
        return self._name

    def get_contact(self):
        return self._contact

    def __str__(self):
        return "Speaker name: {0}, contact: {1}".format(self._name, self._contact)
