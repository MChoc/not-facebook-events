from datetime import datetime

class InputError(Exception):
    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Creating events error occurs with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg)
        self.errors = errors

class SignUpError(Exception):

    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Login error occurs with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg)
        self.errors = errors

#not using at the moment
class LoginError(Exception):

    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Login error occurs with fields: %s"%(', '.join(errors.keys()))
        super().__init__(msg)
        self.errors = errors


def check_creating_seminar_error(name, status, abstractInfo, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sfee, searlyRegDate, sabstractInfo, speaker_name, speaker_email):
    errors = {}
    date_format = "%Y-%m-%d"
    time_format = "%H:%M"

    try:
        datetime.strptime(sdate, date_format)
    except:
        errors['sdate'] = 'Please specify a valid session date.'
    
    try:
        datetime.strptime(stime, time_format)
    except:
        errors['stime'] = 'Please specify a valid session time.'
    
    try:
        datetime.strptime(sdeRegWindow, date_format)
    except:
        errors['sdeRegWindow'] = 'Please specify a valid deregistration date.'
    
    try:
        datetime.strptime(searlyRegDate, date_format)
    except:
        errors['searlyRegDate'] = 'Please specify a valid early bird registration date.'
    
    if name == '':
        errors['name'] = 'Please specify a valid seminar name.'
    if status == '':
        errors['status'] = 'Please specify a valid seminar status.'
    if abstractInfo == '':
        errors['abstractInfo'] = 'Please specify a valid seminar abstract information.'
    if sname == '':
        errors['sname'] = 'Please specify a valid session name.'
    if sstatus == '':
        errors['sstatus'] = 'Please specify a valid session status.'
    if slocation == '':
        errors['slocation'] = 'Please specify a valid session location.'
    if smaxAttendees == '':
        errors['smaxAttendees'] = 'Please specify a valid session capacity.'
    if sfee == '':
        errors['sfee'] = 'Please specify a valid session fee.'
    if sabstractInfo == '':
        errors['sabstractInfo'] = 'Please specify a valid session abstract information.'
    if speaker_name == '':
        errors['speaker_name'] = 'Please specify a valid speaker name.'
    if speaker_email == '':
        errors['speaker_email'] = 'Please specify a valid speaker email.'

    if 'sdeRegWindow' not in errors and 'sdate' not in errors:
        if datetime.strptime(sdeRegWindow, date_format).date() > datetime.strptime(sdate, date_format).date():
            errors['dereg'] = 'Please specify a valid deregistration date'
    if 'searlyRegDate' not in errors and 'sdate' not in errors:
        if datetime.strptime(searlyRegDate, date_format).date() > datetime.strptime(sdate, date_format).date():
            errors['earlybird'] = 'Please specify a valid early bird registration date'

    if 'smaxAttendees' not in errors:
        if int(smaxAttendees) < 1:
            errors['invalid_capacity'] = 'Please specify a valid session capacity.'
    if 'sfee' not in errors:
        if int(sfee) < 0:
            errors['invalid_fee'] = 'Please specify a valid session registration fee.'    
    
    return errors

def check_creating_course_error(name, status, date, time, location, maxAttendees, deRegWindow, fee, earlyRegDate, abstractInfo):
    errors = {}
    date_format = "%Y-%m-%d"
    time_format = "%H:%M"

    try:
        datetime.strptime(date, date_format)
    except:
        errors['date'] = 'Please specify a valid course date.'
    
    try:
        datetime.strptime(time, time_format)
    except:
        errors['time'] = 'Please specify a valid course time.'
    
    try:
        datetime.strptime(deRegWindow, date_format)
    except:
        errors['deRegWindow'] = 'Please specify a valid deregistration date.'
    
    try:
        datetime.strptime(earlyRegDate, date_format)
    except:
        errors['earlyRegDate'] = 'Please specify a valid early bird registration date.'
    
    if name == '':
        errors['name'] = 'Please specify a valid course name.'
    if status == '':
        errors['status'] = 'Please specify a valid course status.'
    if abstractInfo == '':
        errors['abstractInfo'] = 'Please specify a valid course abstract information.'
    if location == '':
        errors['location'] = 'Please specify a valid course location.'
    if maxAttendees == '':
        errors['maxAttendees'] = 'Please specify a valid course capacity.'
    if fee == '':
        errors['fee'] = 'Please specify a valid course fee.'
    
    if 'deRegWindow' not in errors and 'date' not in errors:
        if datetime.strptime(deRegWindow, date_format).date() > datetime.strptime(date, date_format).date():
            errors['dereg'] = 'Please specify a valid deregistration date'
    if 'earlyRegDate' not in errors and 'date' not in errors:
        if datetime.strptime(earlyRegDate, date_format).date() > datetime.strptime(date, date_format).date():
            errors['earlybird'] = 'Please specify a valid early bird registration date'

    if 'maxAttendees' not in errors:
        if int(maxAttendees) < 1:
            errors['invalid_capacity'] = 'Please specify a valid course capacity.'
    if 'fee' not in errors:
        if int(fee) < 0:
            errors['invalid_fee'] = 'Please specify a valid course registration fee.'    
    
    return errors

def check_guest_registering_error(username, email, password):
    errors = {}

    if username == '':
        errors['username'] = "Specify a valid username"
    if email == '':
        errors['email'] = "Specify a valid email"
    if password == '':
        errors['password'] = "Specify a valid password"

    return errors

#not using at the moment
def check_login_error(username, password):
    errors = {}

    if username == '':
        errors['username'] = "Specify a valid username"

    if password == '':
        errors['password'] = "Specify a valid password"

    return errors
