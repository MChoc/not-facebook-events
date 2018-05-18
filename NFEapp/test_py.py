import unittest
import pytest
from models.Student import Student
from server import system
from models.EMS import *
from models.InputError import *

@unittest.skip('not testing')
class CreateCourseTestCase(unittest.TestCase):
    def setUp(self):
        self.staff = system.getUNSWMember('name4119988')
        
    def test_invalid_course_name(self):
        with pytest.raises(InputError) as err:
            system.create_open_course(self.staff, None, 'open', '2018-05-25', '18:15', "CLB7", 15, '2018-05-23', 30, '2018-05-14', "A conversation.")

    def test_invalid_course_status(self):
        with pytest.raises(InputError) as err:
            system.create_open_course(self.staff, "Conversation with Jenny Zhang", None, '2018-05-25', '18:15', "CLB7", 15, '2018-05-23', 30, '2018-05-14', "A conversation.")
 

class CreateSeminarTestCase(unittest.TestCase):
    def setUp(self):
        self.staff = system.getUNSWMember('name4119988')
        #to test if student can create seminar??
        self.student = system.getUNSWMember('name6119988')
        
    #speaker name and speaker email mismatched
    def test_invalid_speaker(self):
        with pytest.raises(InputError) as err:
            system.create_open_seminar(self.staff, 'New College presents', 'open', "some abstract information", 'Session 1', 'open', '2018-05-23', '21:30', 'New College, UNSW', 5, '2018-05-22', 20, '2018-05-20','Opening night', 'Boy 2', 'boy1@unsw.edu.au')

if __name__=='__main__':
    unittest.main()