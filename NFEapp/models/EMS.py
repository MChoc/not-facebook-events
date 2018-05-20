import csv
from .Course import *
from .Seminar import *
from .Staff import *
from .Student import *
from .Guest import *
from .Error import *

class EMS:
    __id = -1  #course/event id
    __sid = -1 #session id

    def __init__(self):
        self._openEvent = []
        self._closeEvent = []
        self._UNSWMember = []
        self._guest = []

    @property
    def openEvent(self):
        return self._openEvent

    @property
    def closeEvent(self):
        return self._closeEvent
    
    @property
    def UNSWMember(self):
        return self._UNSWMember

    @property
    def guest(self):
        return self._guest

    def _generate_id(self):
        EMS.__id += 1
        return EMS.__id

    def _generate_sid(self):
        EMS.__sid += 1
        return EMS.__sid

    def addOpenEvent(self, event):
        self.openEvent.append(event)

    def removeOpenEvent(self,event):
        self.openEvent.remove(event)

    #search open events
    #pass in key words
    #return a list of events whose name contains that key words
    def search_open_events(self, name):
        current_list = []
        for event in self.openEvent:
            if name.lower() in event.name.lower():
                current_list.append(event)
        return current_list

    def addUNSWMember(self, member):
        self.UNSWMember.append(member)

    def addGuest(self, guest):
        self.guest.append(guest)

    def getUNSWMember(self, username):
        for person in self.UNSWMember:
            if person.username == username:
                return person
        return None

    def get_guest_by_email(self, email):
        for person in self.guest:
            if email.lower() == person.email.lower():
                return person

        for person in self.UNSWMember:
            if isinstance(person, Staff):
                if email.lower() == person.email.lower():
                    return person
        return None
    
    def getOpenEvent(self, name):
        for event in self.openEvent:
            if event.name == name:
                return event
        return None

    def getAllEvent(self, id):
        for event in self.openEvent:
            if id == event.id:
                return event
        for event in self.closeEvent:
            if id == event.id:
                return event

    def create_open_course(self, user, name, status, date, time, location, maxAttendees, deRegWindow, fee, earlyRegDate, abstractInfo):
        date_format = "%Y-%m-%d"
        time_format = "%H:%M"

        errors = check_creating_course_error(name, status, date, time, location, maxAttendees, deRegWindow, fee, earlyRegDate, abstractInfo)
        if errors != {}:
            raise InputError(errors)
        else:
            date = datetime.strptime(date, date_format).date()
            time = datetime.strptime(time, time_format).time()
            deRegWindow = datetime.strptime(deRegWindow, date_format).date()
            earlyRegDate = datetime.strptime(earlyRegDate, date_format).date()
            maxAttendees = int(maxAttendees)
            fee = int(fee)
        
            id = self._generate_id()
            course = Course(id, name, status, date, time, location, maxAttendees, deRegWindow, fee, earlyRegDate, abstractInfo)
            user.createCourse(course)
            self.addOpenEvent(course)

    def create_open_seminar(self, user, name, status, abstractInfo, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sfee, searlyRegDate, sabstractInfo, speaker_name, speaker_email):
        date_format = "%Y-%m-%d"
        time_format = "%H:%M"
        
        errors = check_creating_seminar_error(name, status, abstractInfo, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sfee, searlyRegDate, sabstractInfo, speaker_name, speaker_email)
        if errors == {}:
            if not self.get_guest_by_email(speaker_email):
                errors['ineligibleSpeaker'] = 'Please specify an eligible speaker'
            if 'ineligibleSpeaker' not in errors:
                if self.get_guest_by_email(speaker_email).username != speaker_name:
                    errors['speakerMismatch'] = 'Speaker email and name not match'
        if errors != {}:
            raise InputError(errors)
        else:
            sdate = datetime.strptime(sdate, date_format).date()
            sdeRegWindow = datetime.strptime(sdeRegWindow, date_format).date()
            searlyRegDate = datetime.strptime(searlyRegDate, date_format).date()
            smaxAttendees = int(smaxAttendees)
            sfee = int(sfee)

            speaker= self.get_guest_by_email(speaker_email)
            id = self._generate_id()
            sid = self._generate_sid()
            seminar = Seminar(id, name, status, abstractInfo)
            session = Session(sid, sname, sstatus, sdate, stime, slocation, int(smaxAttendees), sdeRegWindow, int(sfee), searlyRegDate,  sabstractInfo, speaker)
            user.createSeminar(seminar, session)
            self.addOpenEvent(seminar)

    def add_session(self, user, seminar, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sfee, searlyRegDate, sabstractInfo, speaker_name, speaker_email):
        date_format = "%Y-%m-%d"
        time_format = "%H:%M"
        
        seminar = seminar
        errors = check_creating_seminar_error(seminar.name, seminar.status, seminar.abstractInfo, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sfee, searlyRegDate, sabstractInfo, speaker_name, speaker_email)

        if errors == {}:
            if not self.get_guest_by_email(speaker_email):
                errors['ineligibleSpeaker'] = 'Please specify an eligible speaker'
            if 'ineligibleSpeaker' not in errors:
                if self.get_guest_by_email(speaker_email).username != speaker_name:
                    errors['speakerMismatch'] = 'Speaker email and name not match'
        if errors != {}:
            raise InputError(errors)
        else:
            sdate = datetime.strptime(sdate, date_format).date()
            sdeRegWindow = datetime.strptime(sdeRegWindow, date_format).date()
            searlyRegDate = datetime.strptime(searlyRegDate, date_format).date()
            smaxAttendees = int(smaxAttendees)
            sfee = int(sfee)

            if user.avoid_creator(seminar) == True:
                return False
            
            speaker= self.get_guest_by_email(speaker_email)
            sid = self._generate_sid()
            session = Session(sid, sname, sstatus, sdate, stime, slocation, smaxAttendees, sdeRegWindow, sfee, searlyRegDate, sabstractInfo, speaker)
            user.addSession(seminar, session)

    def change_course_status(self, user, course, status):
        if user.changeCourseStatus(course, status) == False:
            return False
        self.removeOpenEvent(course)
        self.closeEvent.append(course)

    def change_seminar_status(self, user, seminar, status):
        if user.changeSeminarStatus(seminar, status) == False:
            return False
        self.removeOpenEvent(seminar)
        self.closeEvent.append(seminar)

    def change_session_status(self, user, seminar, session, status):
        if user.changeSessionStatus(seminar, session, status) == False:
            return False

    def register_course(self, user, course):
        if user.registerCourse(course) == False:
            return False

    def register_seminar(self, user, seminar, session):
        if user.registerSeminar(seminar, session) == False:
            return False

    def deRegister_course(self, user, course):
        if user.deRegisterCourse(course) == False:
            return False

    def deRegister_seminar(self, user, seminar):
        if user.deRegisterSeminar(seminar) == False:
            return False

    def deRegister_session(self, user, seminar, session):
        if user.deRegisterSession(seminar, session) == False:
            return False

    def get_current_session(self, user, seminar):
        if user.get_current_session(seminar) == False:
            return False
        return user.get_current_session(seminar)

    def validate_login(self, username, password):

        for c in self.UNSWMember:
            if c.username == username and c.check_password(password):
                return c
        for g in self.guest:
            if g.email == username and g.check_password(password):
                return g
        return None

    def get_user_by_id(self, user_id):
        for c in self.UNSWMember:
            if c.get_id() == user_id:
                return c
        
        for g in self.guest:
            if g.get_id() == user_id:
                return g        
        return None

    def check_capacity(self, event):
        if len(event.attendeeList) < event.maxAttendees:
            return True
        else:
            return False
    
    def check_deregister_validation(self, event):
        currentDate = datetime.now().date()
        if currentDate > event.deRegWindow:
            return False
        else:
            return True

    #pass in either a course or a session
    def check_reg_fee(self, guest, event):
        if isinstance(event, Course):
            return guest.calculate_fee(event)
        else:
            #if the guest is the speaker of the session
            if not guest.avoid_speaker(event):
                return 0
            else:
                for seminar in self.openEvent:
                    #to get seminar id of the session
                    if isinstance(seminar, Seminar) and event in seminar.session:
                        target_id = seminar.id
                        if target_id in guest.assigned_session.values():
                            return 0
                return guest.calculate_fee(event)
                    
    def check_sign_up_history(self, username, email):
        with open('guest.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                name = row[0]
                Email = row[1]
                if username.lower() == name.lower():
                    return False
                if email.lower() == Email.lower():
                    return False
        return True

    def guest_sign_up(self, username, email, password):
        errors = check_guest_registering_error(username, email, password)
        
        if not self.check_sign_up_history(username, email):
            errors['exist'] = 'Account already exists!'        
        
        if errors != {}:
            raise SignUpError(errors)
        else:
            f = open('guest.csv', 'a')
            writer = csv.writer(f)
            writer.writerow((username, email, password))
            f.close()
            self.addGuest(Guest(username, email, password))