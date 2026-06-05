from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ListeningHistory(db.Model):

    __tablename__ = "listening_history"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    song_id = db.Column(db.Integer)

    listened_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )