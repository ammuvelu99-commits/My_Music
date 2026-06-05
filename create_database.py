import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT
)
""")

cursor.execute("""
CREATE TABLE albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER,
    title TEXT,
    FOREIGN KEY (artist_id) REFERENCES artists(id)
)
""")

cursor.execute("""
CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER,
    album_id INTEGER,
    title TEXT,
    file_url TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")