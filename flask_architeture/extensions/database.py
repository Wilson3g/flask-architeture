from flask_sqlalchemy import SQLAlchemy, BaseQuery

db = SQLAlchemy()

def init_app(app):
    return SQLAlchemy(app)