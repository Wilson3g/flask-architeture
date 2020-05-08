from flask_architeture.extensions.database import db
from .user import User
import datetime


class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    path_file = db.Column(db.String(255), nullable=False)
    # user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, server_onupdate=db.func.now())

    def __init__(self, name, path_file):
        self.name = name
        self.path_file = path_file
        # self.user_id = user_id