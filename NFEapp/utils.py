from flask import redirect, url_for
from routes import current_user
from functools import wraps
from models.Staff import Staff
from models.EMS import EMS

def admin_required(f):
    """This is used to check the admin status of the user"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Need to get the instance of the user
        # manually as current_user is of
        # instance werkzeug.local.LocalProxy
        user = get_user_by_id(current_user.id)
        if not isinstance(user, Admin):
            return redirect(url_for('page_not_found'))
        return f(*args, **kwargs)
    return decorated_function
