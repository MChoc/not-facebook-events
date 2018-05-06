from flask_login import UserMixin
from abc import ABC, abstractmethod
from werkzeug.security import generate_password_hash, check_password_hash

class Member(UserMixin, ABC):
    __id = -1
    
    @abstractmethod
    def __init__(self, username, password):
        self._id = self._generate_id()
        self._username = username
        self._password = generate_password_hash(password)


    @property
    def username(self):
        return self._username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def id(self):
        return self._id

    def get_id(self):
        return str(self._id)

    def _generate_id(self):
        Member.__id += 1
        return Member.__id

    # def validate_password(self, password):
    #     return password == self._password

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @abstractmethod
    def is_admin(self):
        pass
