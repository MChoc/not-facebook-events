from .UNSWMember import *

class Student(UNSWMember):

    def __init__(self, username, zID, email, password, role):
        UNSWMember.__init__(self, username, zID, email, password, role)

    def is_admin(self):
        return False
