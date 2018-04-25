import csv
from UNSWMember import *
from EMS import *

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
current = system.getUNSWMember('name6119988')
print(current.zID)
