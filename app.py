from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/playlist")
def playlist():
    return render_template("playlist.html")

@app.route("/artist")
def artist():
    return render_template("artist.html")

@app.route("/album")
def album():
    return render_template("album.html")

@app.route("/player")
def player():
    return render_template("player.html")

if __name__ == "__main__":
    app.run(debug=True)