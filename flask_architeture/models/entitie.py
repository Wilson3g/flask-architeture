from flask_architeture.extensions.database import db
import datetime

class Entity(db.Model):
    __tablename__ = 'entities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200))
    # entity = db.relationship('Entity', backref='users_id')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password