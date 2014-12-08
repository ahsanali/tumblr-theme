from functools import wraps
from flask import current_app
from scanner.models import Vendor
from flask.ext.login import current_user

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated():
            return current_app.login_manager.unauthorized()
        if Vendor.query.filter(Vendor.id==current_user.id).count():
            current_user.is_vendor = True
        return func(*args, **kwargs)
    return decorated_view


def vendor_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated() or not Vendor.query.filter(Vendor.id==current_user.id).count():
            return current_app.login_manager.unauthorized()
        current_user.is_vendor = True
        return func(*args, **kwargs)
    return decorated_view