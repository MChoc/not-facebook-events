from UNSWMember import *

class Student(UNSWMember):

    def __init__(self, username, zID, contact, password, role):
        UNSWMember.__init__(self, username, zID, contact, password, role)

