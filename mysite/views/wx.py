from flask import Blueprint

wx_blueprint = Blueprint('wx', __name__)


@wx_blueprint.route('/wx_home')
def home():
    return '123'