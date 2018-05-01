from flask_login import UserMixin
from abc import ABC, abstractmethod

class Member(UserMixin, ABC):
    __id = -1

    def __init__(self, username, password):
        self._id = self._generate_id()
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self._id)

    def _generate_id(self):
        Member.__id += 1

    def validate_password(self, password):
        return self._password == password
