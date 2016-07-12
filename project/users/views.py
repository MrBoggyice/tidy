##################
#### Imports #####
##################
from flask import render_template, Blueprint


################
#### config ####
################
users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


############
## Routes ##
############
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
