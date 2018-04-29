from server import app, valid_time
from flask import request, render_template, redirect, url_for
from validatePass import *

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

	return render_template('dashboard.html',loggedinas= name)

@app.route('/createevent', methods=['POST', 'GET'])
def createvent():
	if (request.method == 'POST'):
		date= request.form["date"]
		time= request.form["time"]
		location= request.form["location"]
		max_attendees= request.form["max_attendees"]
		deregister_timeWindow= request.form["deregister_timeWindow"]
		description= request.form["description"]
		
		return date, time
		
@app.route('/pastevents/<username>', methods=['POST', 'GET'])
def pastevents(username):
	
	f = open("pastevents--admin_1.txt","r")
	
	superstring = ""
	
	for i in f:
		superstring = superstring+i+"		"
	
	return superstring	
	
@app.route('/searchevents/<eventname>', methods=['POST', 'GET'])
def searchevents(eventname):

	return render_template("eventtemplate.html",eventname = eventname)
	
#pass9588