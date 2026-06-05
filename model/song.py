from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):

    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)

    artist_id = db.Column(db.Integer)

    album_id = db.Column(db.Integer)

    title = db.Column(db.String(150))

    file_url = db.Column(db.String(255))

    duration = db.Column(db.Integer)

    play_count = db.Column(db.Integer, default=0)