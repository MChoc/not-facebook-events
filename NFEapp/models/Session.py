class Session(Event):

    def __init__(self, id, name, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo, speaker):
        Seminar.__init__(self, status, date, time, location, attendeeList, maxAttendees, deRegWindow, abstractInfo)
        self._speaker = speaker


##
    # return str: speaker for session
    @property
    def speaker(self):
        return self._speaker

    # changes speaker
    # arg1 Speaker
    @speaker.setter
    def speaker(self, speaker):
        self._speaker = speaker
##
