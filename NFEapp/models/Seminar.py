class Seminar:

    def __init__(self, id, name, status, abstractInfo):
        self._id = id
        self._name = name
        self._status = status
        self._abstractInfo = abstractInfo
        self._session = []
        # special case: self._attendeeList = list[list[UNSWMember]]
        self._attendeeList = []


##
    # return int id
    @property
    def id(self):
        return self._id

    # no setter method for id [users not allowed to change id of events]
##
##
    # return str name
    @property
    def name(self):
        return self._name

    # changes name of seminar
    # arg1 str
    @name.setter
    def name(self, name):
        self._name = name
##
##
    # return str status 'open', 'closed' or 'cancelled'
    @property
    def status(self):
        return self._status

    # changes status of event
    # arg1 str: 'open', 'closed' or 'cancelled'
    # return int: 0 - failed, 1 - success
    valid_statuses = ['open', 'closed', 'cancelled']
    @status.setter
    def status(self, status):
        if status not in valid_statuses:
            return 0
        else:
            self._status = status
            return 1
##
##
    # return str abstractInfo
    @property
    def abstractInfo(self):
        return self._abstractInfo

    # change abstractinfo of event
    # arg1 str
    @abstractInfo.setter
    def abstractInfo(self, abstractInfo):
        self._abstractInfo = abstractInfo
##
##
    # return list[session]
    @property
    def sessions(self):
        return self._session

    # adds session to session list in Seminar
    # arg1 session
    def add_session(self, session):
        self._session.append(session)
    
    def get_one_session(self, name):
        for session in self._session:
            if session.name == name:
                return session
        return None


    # removes input session from list of sessions
    # arg1 session
    # return int: 0 - failed, 1 - success
    def remove_session(self, session):
        if session in self._session:
            self._session.remove(session)
            return 1
        else:
            return 0
##
##
    # return list[list[UNSWMember]] from session
    @property
    def attendeeList(self):
        return self._attendeeList

    # append a list[UNSWMember] from a session
    # arg1 list[UNSWMember] from session
    def add_attendeeList(self, attendeeList):
        self._attendeeList.append(attendeeList)
##
