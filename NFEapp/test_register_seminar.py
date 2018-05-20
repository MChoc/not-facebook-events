import unittest
import pytest
from server import system
from models.Seminar import *
from models.EMS import *
from models.Error import *

#I have no idea why self.assertEqual is not working

class RegisterSeminarTestCase(unittest.TestCase):
    def setUp(self):
        self.staff = system.getUNSWMember('admin_1')
        self.student = system.getUNSWMember('name6119988')
        self.seminar = system.getOpenEvent('New College presents: How to Succeed in Business Without Really Trying')
        self.session = self.seminar.get_one_session('Session 1')
        self.speaker = system.get_guest_by_email('i.carr@unsw.edu.au')
        self.guest = system.get_guest_by_email('xuanyueqing@gmail.com')

    def test_convenor_register(self):
        assert system.register_seminar(self.staff, self.seminar, self.session) == False

    def test_speaker_register(self):
        assert system.register_seminar(self.speaker, self.seminar, self.session) == False

    def test_closed_session(self):
        self.session.status = 'closed'
        assert system.register_seminar(self.student, self.seminar, self.session) == False
        self.session.status = 'open'

    def test_register_twice(self):
        system.register_seminar(self.student, self.seminar, self.session)
        assert system.register_seminar(self.student, self.seminar, self.session) == False