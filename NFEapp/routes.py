from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from server import app, system
from datetime import datetime
from utils import admin_required
from models.Staff import Staff
from models.bootstrap_system import *

@app.route('/')
def landing_page():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('open_events'))
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
    # return render_template('open_events.html', events=system.openEvent)

    course = []
    seminar = []
    for event in system.openEvent:
        if isinstance(event, Course):
            course.append(event)
        elif isinstance(event, Seminar):
            seminar.append(event)

    return render_template('open_events.html', events=system.openEvent, seminar=seminar, course=course)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/create_event', methods=['GET','POST'])
@login_required
@admin_required
def create_event():
    staff = current_user

    if request.method == 'POST':
        date_format = "%Y-%m-%d"
        time_format = "%H:%M"
        name = request.form['name']
        status = request.form['status']
        date = datetime.strptime(request.form['date'], date_format)
        time = datetime.strptime(request.form['time'], time_format)
        location = request.form['location']
        maxAttendees = int(request.form['maxAttendees'])
        deRegWindow = datetime.strptime(request.form['deRegWindow'], date_format)
        abstractInfo = request.form['abstractInfo']

    if 'create' in request.form:
        system.create_open_course(staff, name, status, date, time, location, maxAttendees, deRegWindow, abstractInfo)
        return redirect(url_for('dashboard'))
    return render_template('create_event.html')

@app.route('/<event_id>', methods=['GET','POST'])
@login_required
def event(event_id):
    event = system.getAllEvent(int(event_id))

    if isinstance(event, Course):
        type = 'course'
    elif isinstance(event, Seminar):
        type = 'seminar'

    if request.method == 'POST':
        if 'register_course' in request.form and type == 'course':
            system.register_course(current_user, event)
        elif 'close_course' in request.form:
            system.change_course_status(current_user, event, 'closed')
        elif 'close_seminar' in request.form:
            system.change_seminar_status(current_user, event, 'closed')
        elif 'deregister_course' in request.form:
            print("deregister")
            system.deRegister_course(current_user, event)
        elif 'deregister_seminar' in request.form:
            system.deRegister_seminar(current_user, event)


    if event in current_user.currentEvents:
        register = True
    else:
        register = False

    return render_template('event_detail.html', event=event, type=type, user=current_user, register=register)

@app.route('/<seminar_id>/<session_name>', methods=['GET','POST'])
@login_required
def session(seminar_id, session_name):
    seminar = system.getAllEvent(int(seminar_id))
    for s in seminar.session:
        if session_name == s.name:
            session = s

    if request.method == 'POST':
        if 'register_session' in request.form:
            system.register_seminar(current_user, seminar, session)
        elif 'close' in request.form:
            system.change_session_status(current_user,seminar, session, 'closed')
        elif 'deregister_session' in request.form:
            system.deRegister_session(current_user, seminar, session)

    if seminar in current_user.currentEvents:
        register = True
    else:
        register = False

    return render_template('session_detail.html', seminar=seminar, user=current_user, session=session, register=register)
