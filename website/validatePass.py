import csv
import NFE_HASH

def validateUser(username, password):

	db = open("user.csv","r")
	hashFromFile = ""
	found = 0
	
	


	scanner = csv.DictReader(db)
	for i in scanner:
		if(i["name"] == username):
			found = 1
			hashFromFile = i["password"]
			
	
	
	if(found==0):
		return 404

	password_attempt =  NFE_HASH.NFE_hash(password)
	#print(password_attempt)
	#print(password)
	#print(hashFromFile)
	
	if(password_attempt == hashFromFile):
		#print("user %s validated" %username)
		return 100
	else:
		return 101

#validateUser("admin_1","aaa")