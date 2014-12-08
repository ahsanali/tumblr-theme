from sqlalchemy import Column, types
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from scanner.extensions import db
from scanner.utils import get_current_time
# from .constants import USER, USER_ROLE, ADMIN, INACTIVE, USER_STATUS
from flask.ext.login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(100), nullable=True, unique=False)
    email = Column(db.String(100), nullable=True, unique=True)
    created_time = Column(db.DateTime, default=get_current_time)
    _password = Column('password', db.String(100), nullable=True,info={'label': 'password'})
    fb_id = Column(db.String(100), nullable=True, unique=True)



    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    # Hide password encryption by exposing password field only.
    password = db.synonym('_password',
                          descriptor=property(_get_password,
                                              _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)


    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.filter(db.or_(User.name == login, User.email == login)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated

    @classmethod
    def get_or_create_fb_user(cls,fb_obj):
        user = cls.query.filter(User.fb_id == fb_obj['id'])
        if user.count() == 1:
            return user.first()
        user = cls(name = fb_obj['name'],email=fb_obj['email'],fb_id=fb_obj['id'])
        db.session.add(user)
        db.session.commit()
        return user

class Vendor(User):
    __tablename__ = 'vendors'
    __mapper_args__ = {'polymorphic_identity': 'vendor'}
    id = Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(100), nullable=True)
    image_location = Column(db.String(100), nullable=False)
    category = Column(db.String(100), nullable=False)
    vendor_id = Column(db.Integer, db.ForeignKey("vendors.id"))
    created_time = Column(db.DateTime, default=get_current_time)
    vendor = db.relationship('Vendor', backref = 'products', primaryjoin = "Product.vendor_id == Vendor.id")

class Checkout(db.Model):
    __tablename__ = 'checkouts'

    id = Column(db.Integer, primary_key=True)
    product_id = Column(db.Integer, db.ForeignKey("products.id"))
    user_id = Column(db.Integer, db.ForeignKey("users.id"))
    vendor_id = Column(db.Integer, db.ForeignKey("vendors.id"))
    created_time = Column(db.DateTime, default=get_current_time)
    product = db.relationship('Product', backref = 'products', primaryjoin = "Product.id == Checkout.product_id")
    user = db.relationship('User', backref = 'checkouts', primaryjoin = "Checkout.user_id == User.id")
    vendor = db.relationship('Vendor', primaryjoin = "Checkout.vendor_id == Vendor.id")


class SharedAsset(db.Model):
    __tablename__ = 'shared_assets'

    id = Column(db.Integer, primary_key=True)
    created_time = Column(db.DateTime, default=get_current_time)
    checkout_id = Column(db.Integer, db.ForeignKey("checkouts.id"))
    asset_id = Column(db.Integer, db.ForeignKey("assets.id"))
    asset = db.relationship('Asset', backref = 'assets', primaryjoin = "Asset.id == SharedAsset.asset_id")



class Asset(db.Model):
    __tablename__ = 'assets'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(100), nullable=False)
    user_id = Column(db.Integer, db.ForeignKey("users.id"))
    s3_key = Column(db.String(100), nullable=False)
    rsa_key = Column(db.String(100), nullable=False)
    user = db.relationship('User', backref = 'files', primaryjoin = "Asset.user_id == User.id")




