# from flask.ext.mail import Mail

# mail = Mail()

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_oauth import OAuth
oauth = OAuth()