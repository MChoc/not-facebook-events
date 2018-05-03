from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from server import app, system
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
@app.rout('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        valid_user = system.validate_login(username, password)
        if valid_user is None:
            return redirect(url_for('login', fail=True))
        else:
            print("logging in...")
            login_user(valid_user)
            return redirect(url_for('open_events'))
    return render_template('login.html', fail=request.args.get('fail'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

@app.route('/open_events', methods=['POST', 'GET'])
def open_events():
    return render_template('open_events.html')
