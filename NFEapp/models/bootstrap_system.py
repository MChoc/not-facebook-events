import csv
from EMS import *
from werkzeug.security import generate_password_hash, check_password_hash

def bootstrap_system():
    system = EMS()
    row_list = []
    with open("user.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            username = row[0]
            zID = row[1]
            email = row[2]
            passw = row[3]
            password = generate_password_hash(passw)
            row[3]= password
            #writer.writerow(row[3], password)
            role = row[4]
            row_list.append(row)

    with open("user.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
        
    with open("user.csv", 'r') as file:
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
            
    
    return system
