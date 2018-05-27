import unittest
import pytest
from server import system
from models.Seminar import *
from models.EMS import *
from models.Error import *


# (3) register for a seminar by student
# (4) register for a seminar by guest-user
class RegisterSeminarTestCase(unittest.TestCase):
    def setUp(self):
        self.convener = system.getUNSWMember('admin_1') # Convener of event below
        self.seminar = system.getOpenEvent('New College presents: How to Succeed in Business Without Really Trying')
        self.session1 = self.seminar.get_one_session('Session 1')
        self.session2 = self.seminar.get_one_session('Session 2')
        self.seminarE = system.getOpenEvent('COMP1531')
        self.sessionE1 = self.seminarE.get_one_session('Lesson 1')
        self.staff = system.getUNSWMember('name4119988')
        self.student = system.getUNSWMember('name6119988')
        self.placeholder = system.getUNSWMember('name6119989')
        self.speaker = system.get_guest_by_email('i.carr@unsw.edu.au')
        self.guest = system.get_guest_by_email('xuanyueqing@gmail.com')


# None == True
# Changes to the system in each test case are reverted at the end of the test

## Initial registration

    # Student registering for seminar
    @pytest.mark.run(order=1)
    def test_student_register(self):
        assert system.register_seminar(self.student, self.seminar, self.session1) == None
        system.deRegister_seminar(self.student, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Staff registering for seminar
    @pytest.mark.run(order=2)
    def test_staff_register(self):
        assert system.register_seminar(self.staff, self.seminar, self.session1) == None
        system.deRegister_seminar(self.staff, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Guest registering for seminar
    @pytest.mark.run(order=3)
    def test_guest_register(self):
        assert system.register_seminar(self.guest, self.seminar, self.session1) == None
        system.deRegister_seminar(self.guest, self.seminar)
        assert len(self.session1.attendeeList) == 0

##
## Student specific test cases



##
## Staff specific test cases

    # Convener of event cannot register for own event
    @pytest.mark.run(order=4)
    def test_convenor_register(self):
        assert system.register_seminar(self.convener, self.seminar, self.session1) == False
        assert len(self.session1.attendeeList) == 0

##
## Guest speaker specific test cases

    # Guest speaker cannot register for event if they are the speaker
    @pytest.mark.run(order=5)
    def test_guest_speaker_register(self):
        assert system.register_seminar(self.speaker, self.seminar, self.session1) == False
        assert len(self.session1.attendeeList) == 0

    # Guest speaker gets free registration to other session in the seminar they speak for
    @pytest.mark.run(order=6)
    def test_guest_speaker_register_free(self):
        assert system.register_seminar(self.speaker, self.seminar, self.session2) == None
        self.assertEqual(system.check_reg_fee(self.speaker, self.session2), 0)
        system.deRegister_seminar(self.speaker, self.seminar)
        assert len(self.session2.attendeeList) == 0

##
## Guest specific test cases
    # Only one of these cases can be loaded at a time
    # Early bird window will need to be manually changed to fit realtime date

    # Guest registers for an event before early bird date and pays early bird rate
    @pytest.mark.run(order=7)
    def test_guest_register_earlyFee(self):
        assert system.register_seminar(self.guest, self.seminar, self.session1) == None
        self.assertEqual(system.check_reg_fee(self.guest, self.session1), 10)
        system.deRegister_seminar(self.guest, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Guest registers for an event after early bird date and pays full fee
    @pytest.mark.run(order=8)
    def test_guest_register_fullFee(self):
        assert system.register_seminar(self.guest, self.seminarE, self.sessionE1) == None
        self.assertEqual(system.check_reg_fee(self.guest, self.sessionE1), 20)
        system.deRegister_seminar(self.guest, self.seminarE)
        assert len(self.sessionE1.attendeeList) == 0

##
## Seminar closed test cases

    # Students cannot register for a closed seminar
    @pytest.mark.run(order=9)
    def test_student_register_seminar_closed(self):
        self.seminar.status = 'closed'
        self.session1.status = 'closed'
        self.session2.status = 'closed'
        assert system.register_seminar(self.student, self.seminar, self.session1) == False
        system.deRegister_seminar(self.student, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Staff cannot register for a closed seminar
    @pytest.mark.run(order=10)
    def test_staff_register_seminar_closed(self):
        assert self.seminar.status == 'closed'
        assert self.session1.status == 'closed'
        assert self.session2.status == 'closed'
        assert system.register_seminar(self.staff, self.seminar, self.session1) == False
        system.deRegister_seminar(self.staff, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Guests cannot register for a closed seminar
    @pytest.mark.run(order=11)
    def test_guest_register_seminar_closed(self):
        assert self.seminar.status == 'closed'
        assert self.session1.status == 'closed'
        assert self.session2.status == 'closed'
        assert system.register_seminar(self.guest, self.seminar, self.session1) == False
        self.seminar.status = 'open'
        self.session1.status = 'open'
        self.session2.status = 'open'
        system.deRegister_seminar(self.guest, self.seminar)
        assert len(self.session1.attendeeList) == 0

##
## Session closed test cases
    # Testing session1 closed

    # Students cannot register for a closed session
    @pytest.mark.run(order=12)
    def test_student_register_session_closed(self):
        self.session1.status = 'closed'
        assert system.register_seminar(self.student, self.seminar, self.session1) == False
        system.deRegister_seminar(self.student, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Staff cannot register for a closed session
    @pytest.mark.run(order=13)
    def test_staff_register_session_closed(self):
        assert self.session1.status == 'closed'
        assert system.register_seminar(self.staff, self.seminar, self.session1) == False
        system.deRegister_seminar(self.staff, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Guests cannot register for a closed session
    @pytest.mark.run(order=14)
    def test_guest_register_session_closed(self):
        assert self.session1.status == 'closed'
        assert system.register_seminar(self.guest, self.seminar, self.session1) == False
        self.session1.status = 'open'
        system.deRegister_seminar(self.guest, self.seminar)
        assert len(self.session1.attendeeList) == 0

##
## Session full test cases
    # Testing session1 full

    # Students cannot register for a full session
    @pytest.mark.run(order=15)
    def test_student_register_session_full(self):
        system.register_seminar(self.placeholder, self.seminar, self.session1)
        assert system.register_seminar(self.student, self.seminar, self.session1) == False
        system.deRegister_seminar(self.student, self.seminar)
        assert len(self.session1.attendeeList) == 1

    # Staff cannot register for a full session
    @pytest.mark.run(order=16)
    def test_staff_register_session_full(self):
        assert self.session1.attendeeList[0] == self.placeholder
        system.register_seminar(self.staff, self.seminar, self.session1) == False
        system.deRegister_seminar(self.staff, self.seminar)
        assert len(self.session1.attendeeList) == 1

    @pytest.mark.run(order=17)
    def test_guest_register_session_full(self):
        assert self.session1.attendeeList[0] == self.placeholder
        system.register_seminar(self.guest, self.seminar, self.session1) == False
        system.deRegister_seminar(self.placeholder, self.seminar)
        system.deRegister_seminar(self.guest, self.seminar)
        assert len(self.session1.attendeeList) == 0

##
## User already registered test cases

    # Students cannot register for a session they are already registered for
    @pytest.mark.run(order=18)
    def test_student_register_session_already(self):
        system.register_seminar(self.student, self.seminar, self.session1)
        assert system.register_seminar(self.student, self.seminar, self.session1) == False
        system.deRegister_seminar(self.student, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Staff cannot register for a session they are already registered for
    @pytest.mark.run(order=19)
    def test_staff_register_session_already(self):
        system.register_seminar(self.staff, self.seminar, self.session1)
        assert system.register_seminar(self.staff, self.seminar, self.session1) == False
        system.deRegister_seminar(self.staff, self.seminar)
        assert len(self.session1.attendeeList) == 0

    # Guests cannot register for a session they are already registered for
    @pytest.mark.run(order=20)
    def test_guest_register_session_already(self):
        system.register_seminar(self.guest, self.seminar, self.session1)
        assert system.register_seminar(self.guest, self.seminar, self.session1) == False
        system.deRegister_seminar(self.guest, self.seminar)
        assert len(self.session1.attendeeList) == 0

##
