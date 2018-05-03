from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from server import app, system
from datetime import datetime
from utils import admin_required


@app.route('/')
def landing_page():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
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
            fail=False
            return redirect(url_for('open_events'))
    return render_template('login.html', fail=request.args.get('fail'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('landing_page'))


@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404


@app.route('/open_events')
@login_required
def open_events():
    return render_template('open_events.html', events=system.openEvent)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/create_event')
@login_required
@admin_required
def create_event():
    return render_template('create_event.html')
