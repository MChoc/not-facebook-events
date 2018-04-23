class Session(Seminar):

    def __init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, session, speaker):
        Seminar.__init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, session)
        self._session = session

    def get_speaker():
        return 0 # TODO:
