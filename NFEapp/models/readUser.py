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
'''
#below are tests for courses

#create event test
staff = current
print(staff.get_current_post_event())

#(name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo, type)
staff.createEvent('acct','open',04.19,19.00,'unsw',15,'24hr','new','course',system)
print('current post: {0}'.format(staff.get_current_post_event()))
event1 = system.getOpenEvent('acct')
print('systems open event: {0}'.format(system._openEvent))
print(event1.get_name())

#change status of event:acct
#staff.changeStatus(event1, 'closed', system)
print('current post: {0}'.format(staff.get_current_post_event()))
print('systems open event: {0}'.format(system._openEvent))

#register for an event:acct test
#status closed, but can still register!!!!!!!!!
student = system.getUNSWMember('name6119989')
print('current enroll: {0}'.format(student.get_current_event())) #which is null

print("register")
print(student.registerCourse(event1))
print('current enroll: {0}'.format(student.get_current_event()))

print('attendee: {0}'.format(event1.get_attendeeList()))
staff.changeStatus(event1, 'closed', system)


#register event:acct again to check duplication
print("register again")
print(student.registerCourse(event1))
print('attendee: {0}'.format(event1.get_attendeeList()))

#deregister from event:acct test
#student.deRegister(event1)
print('attendee: {0}'.format(event1.get_attendeeList()))

#the person who created this event registers for this event
print("creator registration")
print(staff.registerCourse(event1))

print("current event:")
for e in staff.get_current_event():
    print(e.get_name())

print("current post event:")
for e in staff.get_current_post_event():
    print(e.get_name())
'''

#below are tests for seminar and sessions
#create a seminar
staff = current
staff.createEvent('infs', 'open', 04.20, 17.00, 'mel', 14, '12hr', 'good', 'seminar',system)
staff2.createEvent('fins', 'open', 04.20, 17.00, 'mel', 14, '12hr', 'good', 'seminar',system)
print('current post: {0}'.format(staff.get_current_post_event()))

#add a session into the seminar
    #name, date, time, location, maxAttendees, deRegWindow, abstractInfo, sessionStatus, speaker
seminar1 = system.getOpenEvent('infs')
seminar2 = system.getOpenEvent('fins')

seminar1.add_session('infs2608', 04.25, 16.00, 'asb', 5, '5hr', 'database','open', Speaker('Tom', 'hello@gmail.com'))
seminar1.add_session('infs2609', 04.25, 16.00, 'asb', 5, '5hr', 'database','open', Speaker('Jaze', 'hi@gmail.com'))
seminar1.add_session('infs2605', 04.25, 16.00, 'asb', 5, '5hr', 'database','open', Speaker('Jaze', 'hi@gmail.com'))
seminar2.add_session('fins1613', 04.25, 16.00, 'asb', 5, '5hr', 'database','open', Speaker('Tom', 'hello@gmail.com'))

for session in seminar1.get_all_session():
    print(session.get_speaker())

student = system.getUNSWMember('name6119989')
session1 = seminar1.get_one_session('infs2608')
session2 = seminar1.get_one_session('infs2609')
session3 = seminar1.get_one_session('infs2605')
session4 = seminar2.get_one_session('fins1613')

staff.change_session_status(seminar1, session1, 'closed')

print(staff.get_current_post_event())
print(staff.get_past_post_event())

print(student.registerSeminar(seminar1, session1))
student.registerSeminar(seminar1, session2)
student.registerSeminar(seminar1, session3)
#print(student.registerSeminar(seminar1, session1)) #return false

for seminar in student.get_current_event():
    print(seminar.get_name())

#staff.changeStatus(seminar1, 'closed', system)
print(student.get_current_event())
print(student.get_past_event())


print('session name: ')
for session in student.get_current_session(seminar1):
    print (session.get_name())


#deregister from seminar and thus all sessions in that seminar
#student.deRegister(seminar1)
#print(student.get_current_event())
#print(student.get_current_session(seminar1))

#deregister from one session not whole seminar
student.deRegisterSession(seminar1, session1)
print(student.get_current_event())
print(student.get_current_session(seminar1))

#deregister from one session again
student.deRegisterSession(seminar1, session2)
print(student.get_current_event())
print(student.get_current_session(seminar1))

#deregister from last session
student.deRegisterSession(seminar1, session3)
print(student.get_past_event())
print(student.get_current_session(seminar1))

print("check")
print(staff.registerSeminar(seminar1, session2))
print(staff2.registerSeminar(seminar1, session2))
print(session2.get_attendeeList())

print("staff2 info:")
print(staff2.get_current_post_event())
print(staff2.get_current_event())