class Seminar:

    def __init__(self, id, name, status, abstractInfo):
        self._session = []
        # special case: self._attendeeList = list[list[UNSWMember]]
        self._attendeeList = []


##
    # return list[session]
    @property
    def sessions(self):
        return self._session

    # adds session to session list in Seminar
    # arg1 session
    def add_session(self, session):
        self._session.append(session)

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
