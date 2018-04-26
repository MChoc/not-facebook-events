from server import app, valid_time
from flask import request, render_template, redirect, url_for



@app.route('/', methods=['POST', 'GET'])
def landingPage():
	if (request.method == 'POST'):
		username = request.form["username"]
		if(username == "hi"):
			return redirect(url_for("dashboard"))

	return render_template('loginpage.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
	
	return render_template('dashboard.html')
