from flask import Flask
from flask_login import LoginManager
from models.bootstrap_system import bootstrap_system

app = Flask(__name__)
app.secret_key = 'secret_key'
system = bootstrap_system()

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return system.get_user_by_id(user_id)
