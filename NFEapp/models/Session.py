class Session(Seminar):

    def __init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, session, speaker):
        Seminar.__init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, session)
        self._speaker = speaker

    def get_speaker(self):
        return self._speaker

    def set_speaker(self, speaker):
        self._speaker = speaker
