from flask_architeture.extensions.database import db
import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, server_onupdate=db.func.now())
    # entity = db.relationship('Entity', backref='users_id')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
