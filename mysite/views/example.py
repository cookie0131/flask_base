from flask import Blueprint

example_blueprint = Blueprint('example', __name__)


@example_blueprint.route('/home')
def home():
    return '123'