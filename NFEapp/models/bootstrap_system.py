import csv
from .EMS import *

def bootstrap_system():
    system = EMS()

    with open("user.csv", "r") as file:
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

    with open("guest.csv", "r") as guest_file:
        reader = csv.reader(guest_file, delimiter=',')
        for row in reader:
            username = row[0]
            email = row[1]
            password = row[2]
            system.addGuest(Guest(username, email, password))

    system.create_open_course(system.getUNSWMember('admin_1'), "Conversation with Jenny Zhang", 'open', '2018-05-19', '18:15', "CLB7", 15, '2018-05-17', 30, '2018-05-17',
    "A conversation on campus with New York based poet, writer and performer Jenny Zhang as part of Sydney Writers’ Festival 2018.")
    system.create_open_course(system.getUNSWMember('admin_1'), "Free lunch hour concert May - Australia Ensemble",'open','2018-06-27','13:10','John Niland Scientia Building',20,'2018-06-26', 15, '2018-06-25',
    "Bask in the beautiful sounds of one of the country’s leading chamber ensembles, as the Australia Ensemble present a free lunch hour concert.")
    system.create_open_seminar(system.getUNSWMember('admin_1'), 'New College presents: How to Succeed in Business Without Really Trying', 'open', "In the early 1960s, young window-cleaner, J. Pierrepont Finch discovers a book with instructions on how to climb to the top of the company ladder. But it's not long before Finch’s unorthodox and morally questionable business practices jeopardize not only his career but also his flowering romance with Secretary Rosemary Pilkington. New College productions are known for their particularly entertaining atmosphere and high production quality, so please come along!", 'Session 1', 'open', '2019-06-23', '21:30', 'New College, UNSW', 1, '2019-06-22', 20, '2018-06-20','Opening night', 'Isaac Carr', 'i.carr@unsw.edu.au')
    system.add_session(system.getUNSWMember('admin_1'), system.getOpenEvent('New College presents: How to Succeed in Business Without Really Trying'), 'Session 2', 'open', '2018-06-24', '21:30', 'New College, UNSW', 5, '2018-06-23', 10, '2018-06-20', 'Middle night', 'Boy 2', 'boy2@unsw.edu.au')
    system.add_session(system.getUNSWMember('admin_1'), system.getOpenEvent('New College presents: How to Succeed in Business Without Really Trying'), 'Session 3', 'open', '2018-06-25', '21:30', 'New College, UNSW', 5, '2018-06-24', 10, '2018-06-20', 'Closing night', 'Boy 3', 'boy3@unsw.edu.au')

    staff1 = system.getUNSWMember('name4119998')
    staff2 = system.getUNSWMember('name4119997')
    staff3 = system.getUNSWMember('name4119995')
    system.create_open_course(staff1, "Economic Inequality: From Wisconsin to Whyalla",'open','2018-06-29','10:00','Carriageworks',15,'2018-06-29', 40, '2018-06-28',
    "Economic inequality is on the rise in America and in Australia. Middle-class jobs are disappearing, especially in towns that relied on manufacturing. Where does this leave people in affected industries and areas, and the generation to follow? And what are the political implications for democracies? Join author Don Watson, Pulitzer Prize–winning writer Amy Goldstein and UNSW economist Richard Holden in conversation with ABC’s Chief Economics Correspondent Emma Alberici.")
    system.create_open_seminar(staff1, 'COMP1531', 'open', "This course provides an introduction to software engineering principles: software life-cycle concepts, modern development methodologies including XP, Scrum etc., conceptual modeling and how these activities relate to programming. The students are exposed to agile software practices, team collaboration and effective communication through implementing a group project based on agile software methodologies that requires them to analyse, design, build and deploy a web-based application. This course is typically taken in the semester after completing COMP 1511, but could be delayed and taken later. It provides essential background for the teamwork and project management required in many later courses.",
    'Lesson 1', 'open', '2018-06-30', '17:00', 'Mathews Theatre A', 5, '2018-06-25', 20, '2018-06-19', 'Python', 'Isaac Carr', 'i.carr@unsw.edu.au')
    system.create_open_seminar(staff2, 'CVEN3501', 'open', "Water Resources Engineering will provide the basic information describing the hydrological cycle and those components of it that are essential to engineering design and process understanding.",
    'Lesson 1', 'open', '2018-06-24', '17:00', 'Sir John Clancy Auditorium', 5, '2018-06-19', 20, '2018-06-22', 'Water Cycle', 'name4119998', 'z4119998@unsw.net')

    system.create_open_seminar(staff3, 'Effect of CSR Information Presentation Order on Stakeholder Decision‐Making', 'open', 'Stakeholder demand for information about broader social and environmental dimensions of organizational performance is growing', 'Corporate Social Responsibility', 'open', '2018-06-25','16:00', 'Tyree Energy Technology LG07', 15, '2018-06-18', 30, '2018-06-16', 'Socially responsible investment strategies', 'Jaze Zhang', 'zhangting@gmail.com')
    seminar1 = system.getOpenEvent('Effect of CSR Information Presentation Order on Stakeholder Decision‐Making')
    system.add_session(staff3, seminar1, 'Public Enforcement Reputation and the Dual Role of Investor Litigation', 'open','2018-06-21', '09:00', 'Room 2063, Quadrangle Building', 7, '2018-06-19', 10, '2018-06-18','How to Succeed in Business Without Really Trying', 'Boy 1', 'boy1@unsw.edu.au')
    system.add_session(staff3, seminar1, 'On the efficient level of inequality in business income', 'open', '2018-06-28', '10:00', '232, UNSW Business School building', 10, '2018-06-15', 10, '2018-06-23', 'Does External Monitoring Affect the Performance of State-Owned Enterprises?', 'Thomas', 'thomas@gmail.com')

    system.register_course(system.getUNSWMember('name6119988'), system.getOpenEvent('Conversation with Jenny Zhang'))    
    
    return system
