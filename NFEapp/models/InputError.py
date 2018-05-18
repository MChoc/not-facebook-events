class InputError(Exception):
    def __init__(self, field, msg):
        if msg is None:
            msg="field error"
        super().__init__()
        self.field = field
        self.msg=msg + field
