from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)

    email = db.Column(db.String(150), unique=True)

    password_hash = db.Column(db.String(255))