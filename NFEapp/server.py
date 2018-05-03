from flask import Flask
from flask_login import LoginManager
from models.bootstrap_system import bootstrap_system

def valid_time(time):
    return time > 0

app = Flask(__name__)
app.secret_key = 'secret_key'
system = bootstrap_system()

# # Login manager
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login
