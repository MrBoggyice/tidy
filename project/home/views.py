##################
#### Imports #####
##################
from flask import render_template, Blueprint

################
#### config ####
################
home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

############
## Routes ##
############


@home_blueprint.route('/', methods=['GET', 'POST'])
@home_blueprint.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@home_blueprint.route('/home')
def home():
    return render_template('home.html')


# @home_blueprint.route('/confirmation')
# def confirmation():
#     return render_template('confirmation.html')
