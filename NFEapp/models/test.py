from bootstrap_system import *

system = bootstrap_system()

staff1 = system.getUNSWMember('name4119998')
print(staff1.__str__())
staff2 = system.getUNSWMember('name4119997')
'''
system.create_open_seminar(staff1, 'infs', 'open', 'good', 'infs2608', 'open', '2018-04-29', '17:00', 'asb', 5, '2018-05-02', 'database', Speaker('Tom', 'hello@gmail.com'))
system.create_open_seminar(staff2, 'fins', 'open', 'good', 'fins1613', 'open', '2018-05-02', '17:00', 'asb', 5, '2018-04-28', 'database', Speaker('Tom', 'hello@gmail.com'))
system.create_open_course(staff1, 'acct','open','2018-04-29', '17:00','unsw',15,'24hr','new')

seminar1 = system.getOpenEvent('infs')
seminar2 = system.getOpenEvent('fins')
event1 = system.getOpenEvent('acct')

system.add_session(staff1, seminar1, 'infs2609', 'open', '2018-04-25', '17:00', 'asb', 5, '2018-05-02', 'database', Speaker('Jaze', 'hi@gmail.com'))
system.add_session(staff1, seminar1, 'infs2605', 'open', '2018-04-25', '17:00', 'asb', 5, '2018-05-02', 'database', Speaker('Jaze', 'hi@gmail.com'))

print(system.openEvent)

student = system.getUNSWMember('name6119989')
session1 = seminar1.get_one_session('infs2608')
session2 = seminar1.get_one_session('infs2609')
session3 = seminar1.get_one_session('infs2605')
session4 = seminar2.get_one_session('fins1613')


print("other people trying changing")
print(system.change_seminar_status(staff2, seminar1, 'closed'))
print(system.change_session_status(staff2, seminar1, session1, 'closed'))

print(staff1.currentPostEvent)
print(staff1.pastPostEvent)
print(system.register_seminar(student, seminar1, session1))
system.register_seminar(student, seminar1, session2)
system.register_seminar(student, seminar1, session3)
print(system.register_seminar(student, seminar1, session3)) #return false
system.register_course(student, event1)

#for event in student.currentEvents:
#    print(event.name)

print("staff trying changing status")
#print(system.change_seminar_status(staff1, seminar1, 'closed'))
#print(system.change_course_status(staff1, event1, 'closed'))
print(seminar1.status)
print(session1.status)

print(student.currentEvents)
print(student.pastEvents)

print('session name: ')
print(system.get_current_session(student, seminar1))
for s in system.get_current_session(student, seminar1):
    print (s.name)

#deregister from seminar and thus all sessions in that seminar
#system.deRegister_seminar(student, seminar1)
#print(student.currentEvents)
#print(system.get_current_session(student, seminar1))

#deregister from one session not whole seminar
system.deRegister_session(student, seminar1, session1)
print(student.currentEvents)
print(system.get_current_session(student, seminar1))


#deregister from one session again
system.deRegister_session(student, seminar1, session2)
print(student.currentEvents)
print(system.get_current_session(student, seminar1))

#deregister from last session
system.deRegister_session(student, seminar1, session3)
print(student.currentEvents)
print(student.pastEvents)
print(system.get_current_session(student, seminar1))

print("check")
print(system.register_seminar(staff1, seminar1, session2)) #return false
print(system.register_seminar(staff2, seminar1, session2))
print(session2.attendeeList)

print("staff2 info:")
print(staff2.currentPostEvent)
print(staff2.currentEvents)
'''

#below are tests for courses

#create event test
#self, id, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo
system.create_open_course(staff1, 'acct','open','2018-04-19','19:00','unsw',15,'2018-05-10','new')
print('current post: {0}'.format(staff1.currentPostEvent))
event1 = system.getOpenEvent('acct')
print('systems open event: {0}'.format(system.openEvent))
print(event1.name)

#register for an event:acct test
student = system.getUNSWMember('name6119989')
print('current enroll: {0}'.format(student.currentEvents)) #which is null

print("register")
print(system.register_course(student, event1))
print('current enroll: {0}'.format(student.currentEvents))

print('attendee: {0}'.format(event1.attendeeList))
system.change_course_status(staff1, event1, 'closed')
print(event1.status)

#register event:acct again to check duplication
print("register again")
print(system.register_course(student, event1)) #return false
print('attendee: {0}'.format(event1.attendeeList))

#deregister from event:acct test
print(system.deRegister_course(student, event1))
print('attendee: {0}'.format(event1.attendeeList))

#the person who created this event registers for this event
print("creator registration")
print(system.deRegister_course(staff1, event1))

print("current event:")
for e in staff1.currentEvents:
    print(e.name)

print("current post event:")
for e in staff1.currentPostEvent:
    print(e.name)

print("past post event:")
for e in staff1.pastPostEvent:
    print(e.name)

#staff.get_attendeeList(event1)

#print(staff2.get_attendeeList(event1))
