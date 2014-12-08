# -*- coding: utf-8 -*-

import os

from utils import make_dir, INSTANCE_FOLDER_PATH


class BaseConfig(object):

    PROJECT = "tumblr"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False



class DefaultConfig(BaseConfig):

    DEBUG = True
    TESTING = False

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = True
    # SQLITE for prototyping.
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + INSTANCE_FOLDER_PATH + '/db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:beta@localhost/scanner'
    # MYSQL for production.
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db?charset=utf8'


    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    # Flask-mail: http://pythonhosted.org/flask-mail/
    # https://bitbucket.org/danjac/flask-mail/issue/3/problem-with-gmails-smtp-server
    MAIL_DEBUG = DEBUG
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Should put MAIL_USERNAME and MAIL_PASSWORD in production under instance folder.
    MAIL_USERNAME = 'gmail_user'
    MAIL_PASSWORD = 'gmail_password'
    MAIL_DEFAULT_SENDER = '%s@gmail.com' % MAIL_USERNAME
    EMAIL_ADDRESSES = ['sn.ahsanali@gmail.com']

    # Flask-openid: http://pythonhosted.org/Flask-OpenID/
    make_dir(INSTANCE_FOLDER_PATH)
    OPENID_FS_STORE_PATH = os.path.join(INSTANCE_FOLDER_PATH, 'openid')
    make_dir(OPENID_FS_STORE_PATH)
    UPLOAD_FOLDER = './scanner/static/uploads'
    RSA_PATH = '/Users/muhammadahsanali/.ssh/id_rsa.pub'
    
    AWS_ACCESS_KEY_ID = 'AKIAJAQTUOIOCTUPNCCQ'
    AWS_SECRET_ACCESS_KEY = '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'
    
    TUMBLR_APP_ID = 'Q4Jbn9GIl1gImjHbV3yjR0YM1QTwFRnP5cfU6cMT5DGpt3K5lE'
    TUMBLR_APP_SECRET = 'aziCSSusIdA8eybR0F5nftYjvDQsDDC81eCyJMSO4B7g9aV4C1'

    DEFAULT_SENDER_EMAIL = 'ahsan@flux7.com'



class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
