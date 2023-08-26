from flask import Flask 
# TODO: import flask_sqlalchemy
# TODO: import flask_login
from flask_wtf.csrf import CSRFProtect
from os import path

# TODO: declare sqlalchemy db here
csrf = CSRFProtect()


def create_app():

    app = Flask(__name__)
    app.config.from_object('config_template.Config')

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # from .models import Users, Expenses

    # TODO: initialise sqlalchemy db here

    # TODO: create sqlalchemy db file

    # TODO: initialise loginmanager

    csrf.init_app(app)
    return app