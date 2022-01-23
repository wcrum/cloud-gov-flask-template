from flask import request
from flask import session
from flask import jsonify
from sqlmodel import select
from sqlmodel import Session as SQLSession
from app.models.user import User
from flask import current_app

def admin_required(f):
    def wraps_admin_required(*args, **kwgs):
        with SQLSession(current_app.engine) as s:
            query = select(User).where(User.access == "Administrator")
            result = s.exec(query)
            return str(result)

        return f(*args, **kwgs)
    return wraps_admin_required