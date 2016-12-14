##################
#### Imports #####
##################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

##################
#### Config ######
##################

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


#from project.users.views import users_blueprint
from project.home.views import home_blueprint
from project.users.views import users_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
