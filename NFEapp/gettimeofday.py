import datetime

def phaseoftheday():
	x = int(datetime.datetime.now().hour)

	if(0 <= x and x <= 10):
		return "Morning"
	elif (11 < x and x <= 17):
		return "Afternoon"
	elif (17 < x and x < 24):
		return "Evening"
	
	