from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Album(db.Model):

    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)

    artist_id = db.Column(db.Integer)

    title = db.Column(db.String(150))

    cover_image = db.Column(db.String(255))