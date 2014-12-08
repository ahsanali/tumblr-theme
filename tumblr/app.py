# -*- coding: utf-8 -*-

import os

from flask import Flask, request, render_template, current_app
from .config import DefaultConfig
from utils import INSTANCE_FOLDER_PATH
from .extensions import db, oauth
# from flask.ext.mail import Message
from views import configure_views


# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)
    app.secret_key = "sdjf98wrlff~*&8s9ua/2118*91()sdf20234!((#-wf,v02ksa==+"
    configure_app(app, config)
    configure_extensions(app)
    configure_views(app)
    
    return app

def configure_extensions(app):
    db.init_app(app)
    # flask-login



def configure_app(app, config=None):
    """Different ways of configurations."""

    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    # http://flask.pocoo.org/docs/config/#instance-folders
    app.config.from_pyfile('production.cfg', silent=True)

    if config:
        app.config.from_object(config)

    # Use instance folder instead of env variables to make deployment easier.
    #app.config.from_envvar('%s_APP_CONFIG' % DefaultConfig.PROJECT.upper(), silent=True)




def configure_error_handlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/forbidden_page.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/page_not_found.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/server_error.html"), 500

# import views.py
