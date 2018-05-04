import csv
from .EMS import *

def bootstrap_system():
    system = EMS()

    with open("/mnt/c/Users/62572/Desktop/COMP1531/test/not-facebook-events/NFEapp/models/user.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            username = row[0]
            zID = row[1]
            email = row[2]
            password = row[3]
            role = row[4]
            if role == 'trainer':
                system.addUNSWMember(Staff(username, zID, email, password, role))
            elif role == 'trainee':
                system.addUNSWMember(Student(username, zID, email, password, role))


    system.create_open_course(system.getUNSWMember('admin_1'), "Conversation with Jenny Zhang", 'open', '2018-05-03', '18:15', "CLB7", 1000, '2018-05-02', "A conversation on campus with New York based poet, writer and performer Jenny Zhang as part of Sydney Writers’ Festival 2018.")
    system.create_open_course(system.getUNSWMember('admin_1'), 'acct','open','2018-04-19','19:00','unsw',15,'2018-05-10','new')
    #
    staff1 = system.getUNSWMember('name4119998')
    staff2 = system.getUNSWMember('name4119997')
    system.create_open_course(staff1, 'acct1','open','2018-04-19','19:00','unsw',15,'2018-05-10','new')
    system.create_open_seminar(staff1, 'infs', 'open', 'good', 'infs2608', 'open', '2018-04-29', '17:00', 'asb', 5, '2018-05-02', 'database', Speaker('Tom', 'hello@gmail.com'))
    system.create_open_seminar(staff2, 'fins', 'open', 'good', 'fins1613', 'open', '2018-05-02', '17:00', 'asb', 5, '2018-04-28', 'database', Speaker('Tom', 'hello@gmail.com'))
    return system
