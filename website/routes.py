from server import app, valid_time
from flask import request, render_template, redirect, url_for
from validatePass import *
from gettimeofday import *

@app.route('/', methods=['POST', 'GET'])
def landingPage():
	if (request.method == 'POST'):
		username = request.form["username"]
		password = request.form["password"]
		attempt = validateUser(username, password)

		if(attempt == 100):
			return redirect(url_for("dashboard",name=username))
		else:
			return render_template("loginpage.html", error_code = attempt)

	return render_template('loginpage.html')

@app.route('/dashboard/<name>', methods=['POST', 'GET'])
def dashboard(name):
	string_time = phaseoftheday()


	pix = 0

	if(string_time == "Morning"):
		pix = 'morningtime.jpg'
	elif(string_time=="Afternoon"):
		pix = 'afternoontime.jpg'
	elif(string_time=="Evening"):
		pix = 'nighttime.jpg'

	return render_template('dashboard.html',loggedinas= name,timeofday= string_time,dashboardpicture=pix)

#@login_required
#@admin_required
@app.route('/createevent', methods=['POST', 'GET'])
def createvent():
	if (request.method == 'POST'):
		date = request.form["date"]
		time = request.form["time"]
		location = request.form["location"]
		max_attendees = request.form["max_attendees"]
		deregister_timeWindow = request.form["deregister_timeWindow"]
		description = request.form["description"]

		# new_event = system.create_open_course(current_user, current_user.username, 'open', date, time, location, max_attendees, deregister_timeWindow, description)

		return date, time
		#return new_event

@app.route('/pastevents/<username>', methods=['POST', 'GET'])
def pastevents(username):
#def pastevents(current_user):

	filePath = r"databases\Users\%s\Past.txt" % (username)
	f = open(filePath,"r")

	superstring = ""

	for i in f:
		superstring = superstring+i+"<br>"



	return superstring
	#return current_user.pastEvents

@app.route('/currentevents/<username>', methods=['POST', 'GET'])
def currentevents(username):

	filePath = r"databases\Users\%s\Current.txt" % (username)
	f = open(filePath,"r")

	superstring = ""

	for i in f:
		superstring = superstring+i+"<br>"

	return superstring

@app.route('/searchevents/<eventname>', methods=['POST', 'GET'])
def searchevents(eventname):

	filePath = r"databases\Events\%s.txt" % (eventname)

	f = open(filePath,"r")

	superstring = ""

	for i in f:
		superstring = superstring+i+"<br>"

	return superstring

	#return render_template("eventtemplate.html",eventname = eventname)

#pass9588
