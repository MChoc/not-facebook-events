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
    course =[]
    seminar = []
    for event in system.openEvent:
        try:
            session1 = event.session
        except AttributeError:
            session1 = None
    
        if not session1:
            course.append(event)
        else:
            seminar.append(event)

    return render_template('open_events.html', event = system.openEvent, seminar = seminar, course = course)


@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    print(current_user.currentEvents)
    if request.method == 'POST':
        if 'close' in request.form:
            print("close")
            #system.change_course_status(currentPostEvent)
    return render_template('dashboard.html', user = current_user)

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

@app.route('/<event_name>', methods=['GET','POST'])
@login_required
def event(event_name):
    event = system.getOpenEvent(event_name)
    try:
        session1 = event.session
    except AttributeError:
        session1 = []
    
    if session1:
        type = 'seminar'
    else:
        type = 'course'
    if request.method == 'POST':
        if 'register_course' in request.form and type == 'course':
            system.register_course(current_user, event)
        elif 'register_session' in request.form and type == 'seminar':
            system.register_seminar(current_user, event, session1[0])

    return render_template('event_detail.html', event = event, type = type)