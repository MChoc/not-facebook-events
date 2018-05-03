from flask import redirect, url_for
from routes import current_user
from functools import wraps
from models.Staff import Staff
from models.EMS import EMS
from models.bootstrap_system import bootstrap_system
from server import system

def admin_required(f):
    """This is used to check the admin status of the user"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Need to get the instance of the user
        # manually as current_user is of
        # instance werkzeug.local.LocalProxy
        user = system.get_user_by_id(current_user.id)
        if not isinstance(user, Staff):
            return redirect(url_for('page_not_found'))
        return f(*args, **kwargs)
    return decorated_function
