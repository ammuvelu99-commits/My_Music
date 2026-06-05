from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):

    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150))

    bio = db.Column(db.Text)

    image = db.Column(db.String(255))