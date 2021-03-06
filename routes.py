from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from server import app, system
from datetime import datetime
from utils import admin_required
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


@app.route('/open_events', methods=['GET','POST'])
@login_required
def open_events():
    course = []
    seminar = []
    for event in system.openEvent:
        if isinstance(event, Course):
            course.append(event)
        elif isinstance(event, Seminar):
            seminar.append(event)

    if request.method == 'POST':
        key_words = request.form['key_words']
        return render_template('open_events.html', events = system.search_open_events(key_words), seminar=seminar, course=course)

    return render_template('open_events.html', events=system.openEvent, seminar=seminar, course=course)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


@app.route('/create_course', methods=['GET','POST'])
@login_required
@admin_required
def create_course():

    if 'create' in request.form:
        try:
            system.create_open_course(current_user, request.form['name'], request.form['status'], request.form['date'], request.form['time'], request.form['location'], request.form['maxAttendees'], request.form['deRegWindow'], request.form['fee'], request.form['earlyRegDate'], request.form['abstractInfo'])
        except InputError as error:
            return render_template('create_course.html', errors = error.errors)
        else:
            return redirect(url_for('dashboard'))
    return render_template('create_course.html')


@app.route('/create_seminar', methods=['GET','POST'])
@login_required
@admin_required
def create_seminar():

    if 'create' in request.form:
        try:
            system.create_open_seminar(current_user, request.form['cname'], request.form['cstatus'], request.form['cabstractInfo'], request.form['name'], request.form['status'], request.form['date'], request.form['time'], request.form['location'], request.form['maxAttendees'], request.form['deRegWindow'], request.form['fee'], request.form['earlyRegDate'], request.form['abstractInfo'], request.form['speaker_name'], request.form['email'])
        except InputError as error:
            return render_template('create_seminar.html', errors = error.errors)
        else:
            return redirect(url_for('dashboard'))
    return render_template('create_seminar.html')


@app.route('/event/<event_id>', methods=['GET','POST'])
@login_required
def event(event_id):
    event = system.getAllEvent(int(event_id))
    message = None

    if isinstance(event, Course):
        type = 'course'
        if not system.check_capacity(event):
            message = 'full'
        if event in current_user.currentEvents and not system.check_deregister_validation(event):
            message = 'deregister invalid'
    elif isinstance(event, Seminar):
        type = 'seminar'

    if request.method == 'POST':
        if 'register_course' in request.form and type == 'course':
            message = "confirm_register_course"
        elif 'confirm_register_course' in request.form and type == 'course':
            system.register_course(current_user, event)
        elif 'close_course' in request.form:
            message = "confirm_close_course"
        elif 'confirm_close_course' in request.form:
            system.change_course_status(current_user, event, 'closed')
        elif 'view_attendees' in request.form:
            message = "view_attendees"
        elif 'close_seminar' in request.form:
            message = "confirm_close_seminar"
        elif 'confirm_close_seminar' in request.form:
            system.change_seminar_status(current_user, event, 'closed')
        elif 'deregister_course' in request.form:
            message = "confirm_deregister_course"
        elif 'confirm_deregister_course' in request.form:
            system.deRegister_course(current_user, event)
            message = None
        elif 'deregister_seminar' in request.form:
            message = "confirm_deregister_seminar"
        elif 'confirm_deregister_seminar' in request.form:
            system.deRegister_seminar(current_user, event)
        elif 'add_session' in request.form:
            return render_template('event_detail.html', event=event, type=type, user=current_user, register=False, add=True)
        elif 'confirm' in request.form:
            try:
                system.add_session(current_user, event, request.form['name'], request.form['status'], request.form['date'], request.form['time'], request.form['location'], request.form['maxAttendees'], request.form['deRegWindow'], request.form['fee'], request.form['earlyRegDate'], request.form['abstractInfo'], request.form['speaker_name'], request.form['email'])
            except InputError as error:
                return render_template('event_detail.html', event=event, type=type, user=current_user, register=False, add=True, errors = error.errors)

    if event in current_user.currentEvents:
        register = True
    else:
        register = False

    return render_template('event_detail.html', event=event, type=type, user=current_user, register=register, message = message)


@app.route('/seminar/<seminar_id>/<session_name>', methods=['GET','POST'])
@login_required
def session(seminar_id, session_name):
    seminar = system.getAllEvent(int(seminar_id))
    message = None

    for s in seminar.session:
        if session_name == s.name:
            session = s

    if not system.check_capacity(session):
        message = 'full'

    if seminar in current_user.currentEvents and not system.check_deregister_validation(session):
        message = 'deregister invalid'

    if request.method == 'POST':
        if 'register_session' in request.form:
            if current_user.is_guest():
                fee = system.check_reg_fee(current_user, session)
            else:
                fee=0
            message = "confirm_register_session"
            return render_template('session_detail.html', seminar=seminar, user=current_user, session=session, register=False, message = message, fee = fee)
        elif 'confirm_register_session' in request.form:
            system.register_seminar(current_user, seminar, session)
        elif 'close' in request.form:
            message = "confirm_close_session"
        elif 'confirm_close_session' in request.form:
            system.change_session_status(current_user,seminar, session, 'closed')
        elif 'deregister_session' in request.form:
            message = "confirm_deregister_session"
        elif 'confirm_deregister_session' in request.form:
            system.deRegister_session(current_user, seminar, session)
            message = None
        elif 'view_attendees' in request.form:
            message = "view_attendees"
    if seminar in current_user.currentEvents and session in system.get_current_session(current_user, seminar):
        register = True
    else:
        register = False
    print(message)
    return render_template('session_detail.html', seminar=seminar, user=current_user, session=session, register=register, message = message)

#guest speaker profile
@app.route('/seminar/<seminar_id>/<session_name>/<guest_speaker_name>')
@login_required
def guest_speaker(seminar_id, session_name, guest_speaker_name):
    speaker = system.getAllEvent(int(seminar_id)).get_one_session(session_name).speaker
    return render_template('speaker_profile.html', speaker = speaker)

@app.route('/register', methods=['GET','POST'])
def guest_register():

    if 'sign_up' in request.form:
        try:
            system.guest_sign_up(request.form['username'], request.form['email'], request.form['password'])
        except SignUpError as error:
            return render_template('guest_register.html', errors = error.errors)
        else:
            return render_template('guest_register.html', message = True)
    return render_template('guest_register.html')
