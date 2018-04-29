import csv
from UNSWMember import *
from EMS import *
from Event import *
from Course import *
from Seminar import *
from Staff import *
from Student import *
from Speaker import *
system = EMS()

with open("user.csv", "r") as file:
    reader = csv.reader(file, delimiter=',')
    names = []
    for row in reader:
        name = row[0]
        zID = row[1]
        email = row[2]
        password = row[3]
        role = row[4]
        if role == 'trainer':
            system.addUNSWMember(Staff(name, zID, email, password, role))
        elif role == 'trainee':
            system.addUNSWMember(Student(name, zID, email, password, role))

#test    
current = system.getUNSWMember('name4119998')
print(current.__str__())
staff2 = system.getUNSWMember('name4119997')

#below are tests for courses

#create event test
staff = current
print(staff.currentPostEvent)

#self, id, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo
staff.createCourse(Course(3, 'acct','open','2018-04-19','19:00','unsw',15,'24hr','new'),system)
print('current post: {0}'.format(staff.currentPostEvent))
event1 = system.getOpenEvent('acct')
print('systems open event: {0}'.format(system._openEvent))
print(event1.name)

#register for an event:acct test
student = system.getUNSWMember('name6119989')
print('current enroll: {0}'.format(student.currentEvents)) #which is null

print("register")
print(student.registerCourse(event1))
print('current enroll: {0}'.format(student.currentEvents))

print('attendee: {0}'.format(event1.attendeeList))
staff.changeCourseStatus(event1, 'closed', system)
print(event1.status)

#register event:acct again to check duplication
print("register again")
print(student.registerCourse(event1))
print('attendee: {0}'.format(event1.attendeeList))

#deregister from event:acct test
student.deRegisterCourse(event1)
print('attendee: {0}'.format(event1.attendeeList))

#the person who created this event registers for this event
print("creator registration")
print(staff.registerCourse(event1))

print("current event:")
for e in staff.currentEvents:
    print(e.name)

print("current post event:")
for e in staff.currentPostEvent:
    print(e.name)

print("past post event:")
for e in staff.pastPostEvent:
    print(e.name)

#staff.get_attendeeList(event1)

#print(staff2.get_attendeeList(event1))

'''
#below are tests for seminar and sessions
#create a seminar
staff = current
#def __init__(self, id, name, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, speaker):
#        Event.__init__(self, id, name, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo)
staff.createSeminar(Seminar(4, 'infs', 'open', '2018-04-29', '17:00', 'mel', 14, '12hr', 'good'), Session(3, 'infs2608', 'open', '2018-04-29', '17:00', 'asb', 5, '5hr', 'database', Speaker('Tom', 'hello@gmail.com')), system)
staff2.createSeminar(Seminar(3, 'fins', 'open', '2018-04-20', '17:00', 'mel', 14, '12hr', 'good'), Session(5, 'fins1613', 'open', '2018-04-29', '17:00', 'asb', 5, '5hr', 'database', Speaker('Tom', 'hello@gmail.com')), system)


seminar1 = system.getOpenEvent('infs')
seminar2 = system.getOpenEvent('fins')

staff.createSeminar(seminar1,Session(5, 'infs2609', 'open', '2018-04-25', '17:00', 'asb', 5, '5hr', 'database', Speaker('Jaze', 'hi@gmail.com')), system)
staff.createSeminar(seminar1,Session(1, 'infs2605', 'open', '2018-04-25', '17:00', 'asb', 5, '5hr', 'database', Speaker('Jaze', 'hi@gmail.com')), system)
print(seminar1.sessions)

staff.createCourse(Course(7, 'acct','open','2018-04-29', '17:00','unsw',15,'24hr','new'),system)
event1 = system.getOpenEvent('acct')
print('current post: {0}'.format(staff.currentPostEvent))

print(system.get_all_open_event())


#seminar1.add_session('infs2608', 04.25, 16.00, 'asb', 5, '5hr', 'database','open', Speaker('Tom', 'hello@gmail.com'))
#seminar1.add_session('infs2609', 04.25, 16.00, 'asb', 5, '5hr', 'database','open', Speaker('Jaze', 'hi@gmail.com'))
#seminar1.add_session('infs2605', 04.25, 16.00, 'asb', 5, '5hr', 'database','open', Speaker('Jaze', 'hi@gmail.com'))
#seminar2.add_session('fins1613', 04.25, 16.00, 'asb', 5, '5hr', 'database','open', Speaker('Tom', 'hello@gmail.com'))

student = system.getUNSWMember('name6119989')
session1 = seminar1.get_one_session('infs2608')
session2 = seminar1.get_one_session('infs2609')
session3 = seminar1.get_one_session('infs2605')
session4 = seminar2.get_one_session('fins1613')

print("other people trying changing")
#print(staff2.change_session_status(seminar1, session1, 'closed'))

print(staff.currentPostEvent)
print(staff.pastPostEvent)

print(student.registerSeminar(seminar1, session1))
student.registerSeminar(seminar1, session2)
student.registerSeminar(seminar1, session3)
print(student.registerSeminar(seminar1, session1)) #return false
student.registerCourse(event1)

for event in student.currentEvents:
    print(event.name)

print("staff trying changing")
#print(staff.changeSeminarStatus(seminar1, 'closed', system))
#print(staff.changeCourseStatus(event1, 'closed', system))
print(seminar1.status)
print(session1.status)

print(student.currentEvents)
print(student.pastEvents)


print('session name: ')
print(student.get_current_session(seminar1))
for s in student.get_current_session(seminar1):
    print (s.name)


#print(staff.get_attendeeList(event1))
#print(staff2.get_attendeeList(event1))



#deregister from seminar and thus all sessions in that seminar
#student.deRegisterSeminar(seminar1)
print(student.currentEvents)
print(student.get_current_session(seminar1))

#deregister from one session not whole seminar
student.deRegisterSession(seminar1, session1)
print(student.currentEvents)
print(student.get_current_session(seminar1))

#deregister from one session again
student.deRegisterSession(seminar1, session2)
print(student.currentEvents)
print(student.get_current_session(seminar1))

#deregister from last session
#student.deRegisterSession(seminar1, session3)
print(student.pastEvents)
print(student.get_current_session(seminar1))

print("check")
print(staff.registerSeminar(seminar1, session2))
print(staff2.registerSeminar(seminar1, session2))
print(session2.attendeeList)

print("staff2 info:")
print(staff2.currentPostEvent)
print(staff2.currentEvents)
'''