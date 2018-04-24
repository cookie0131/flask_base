from flask import Flask
from mysite.extensions import db
from mysite.views.example import example_blueprint
from mysite.views.wx import wx_blueprint


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)

    app.register_blueprint(example_blueprint, url_prefix='/example')
    app.register_blueprint(wx_blueprint, url_prefix='/wx')

    return app

