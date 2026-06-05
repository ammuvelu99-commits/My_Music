from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    title = db.Column(db.String(150))

    description = db.Column(db.Text)