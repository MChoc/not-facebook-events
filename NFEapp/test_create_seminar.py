import unittest
import pytest
from server import system
from models.EMS import *
from models.Error import *

#User Stories 9 - create a seminar with one session

# @unittest.skip('testing seminar')
class CreateSeminarTestCase(unittest.TestCase):
    def setUp(self):
        self.staff = system.getUNSWMember('name4119988')
        self.student = system.getUNSWMember('name6119988')
        #guest speaker
        self.speaker = system.get_guest_by_email('boy1@unsw.edu.au')

        self.open_event_length = len(system.openEvent)
        self.current_post_length = len(self.staff.currentPostEvent)
        self.current_assign_length = len(self.speaker.assigned_session)


    def test_successful_create_seminar(self):
        system.create_open_seminar(self.staff, 'New College presents', 'open',
            "some abstract information", 'Session 1', 'open', '2018-05-23', '21:30',
            'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
            'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == (self.open_event_length + 1)
        assert len(self.staff.currentPostEvent) == (self.current_post_length + 1)
        assert len(self.speaker.assigned_session) == (self.current_assign_length + 1)
        assert len(system.getOpenEvent('New College presents').session) == 1

    #US9-AC9
    def test_speaker_name_and_email_mismatch(self):
        speaker1_name = 'Boy 2'
        speaker2_email = 'boy1@unsw.edu.au'

        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                "some abstract information", 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                speaker1_name, speaker2_email)

        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC8
    def test_speaker_not_registered_in_EMS(self):
        non_registered_speaker_name = 'Micheal'
        non_registered_speaker_email = 'micheal@unsw.edu.au'

        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                non_registered_speaker_name, non_registered_speaker_email)

        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC8
    def test_speaker_is_a_student(self):
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                "some abstract information", 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                self.student.username, self.student.email)

        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC1
    def test_student_attempt_creating_seminar(self):
        with pytest.raises(AttributeError) as err:
            system.create_open_seminar(self.student, 'New College presents', 'open',
                "some abstract information", 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')

        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC1
    def test_guest_attempt_creating_seminar(self):
        with pytest.raises(AttributeError) as err:
            system.create_open_seminar(self.speaker, 'New College presents', 'open',
                "some abstract information", 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_seminar_name(self):
        seminar_name = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, seminar_name, 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_seminar_status(self):
        seminar_status = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', seminar_status,
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_seminar_abstractInfo(self):
        seminar_abstractInfo = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                seminar_abstractInfo, 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_name(self):
        session_name = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', session_name, 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_status(self):
        session_status = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', session_status, '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_date(self):
        session_date = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', session_date, '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_time(self):
        session_time = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', session_time,
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_location(self):
        session_location = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                session_location, 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_capacity(self):
        session_capacity = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', session_capacity, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_deregistration_date(self):
        session_deregistration_date = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, session_deregistration_date, 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_fee(self):
        session_fee = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', session_fee, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_early_bird_date(self):
        session_early_bird_date = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, session_early_bird_date,'Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_session_abstractInfo(self):
        session_abstractInfo = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20', session_abstractInfo,
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_speaker_name(self):
        speaker_name = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                speaker_name, 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC6
    def test_empty_speaker_email(self):
        speaker_email = ''
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', speaker_email)
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC7
    def test_invalid_session_deregistration_date(self):
        session_date = '2018-05-23'
        session_deregistration_date = '2018-05-29'

        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', session_date, '21:30',
                'New College, UNSW', 5, session_deregistration_date, 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC7
    def test_invalid_session_early_bird_date(self):
        session_date = '2018-05-23'
        session_early_bird_date = '2018-05-29'

        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', session_date, '21:30',
                'New College, UNSW', 5, '2018-05-22', 20, session_early_bird_date,'Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC7
    def test_invalid_maxAttendees_with_amount_less_than_1(self):
        session_max_attendees = 0
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', session_max_attendees, '2018-05-22', 20, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length

    #US9-AC7
    def test_invalid_registration_fee_with_amount_less_than_0(self):
        session_fee = -1
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open',
                'some abstract information', 'Session 1', 'open', '2018-05-23', '21:30',
                'New College, UNSW', 5, '2018-05-22', session_fee, '2018-05-20','Opening night',
                'Boy 1', 'boy1@unsw.edu.au')
        assert len(system.openEvent) == self.open_event_length
        assert len(self.staff.currentPostEvent) == self.current_post_length
        assert len(self.speaker.assigned_session) == self.current_assign_length
