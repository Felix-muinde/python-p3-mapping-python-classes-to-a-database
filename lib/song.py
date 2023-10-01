
from config import CONN, CURSOR

class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def save(self):
        query = "INSERT INTO songs (title, artist, album) VALUES (%s, %s, %s)"
        values = (self.title, self.artist, self.album)
        CURSOR.execute(query, values)
        CONN.commit()

    def update(self):
        query = "UPDATE songs SET artist = %s, album = %s WHERE title = %s"
        values = (self.artist, self.album, self.title)
        CURSOR.execute(query, values)
        CONN.commit()

    def delete(self):
        query = "DELETE FROM songs WHERE title = %s"
        values = (self.title,)
        CURSOR.execute(query, values)
        CONN.commit()

    @classmethod
    def find_by_title(cls, title):
        query = "SELECT * FROM songs WHERE title = %s"
        values = (title,)
        CURSOR.execute(query, values)
        song_data = CURSOR.fetchone()
        if song_data:
            return cls(*song_data)
        else:
            return None

    @classmethod
    def all(cls):
        query = "SELECT * FROM songs"
        CURSOR.execute(query)
        songs_data = CURSOR.fetchall()
        return [cls(*song_data) for song_data in songs_data]
