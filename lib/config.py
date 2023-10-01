
import sqlite3

# Create a database connection
CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def save(self):
        query = "INSERT INTO songs (title, artist, album) VALUES (?, ?, ?)"
        values = (self.title, self.artist, self.album)
        CURSOR.execute(query, values)
        CONN.commit()

    def update(self):
        query = "UPDATE songs SET artist = ?, album = ? WHERE title = ?"
        values = (self.artist, self.album, self.title)
        CURSOR.execute(query, values)
        CONN.commit()

    def delete(self):
        query = "DELETE FROM songs WHERE title = ?"
        values = (self.title,)
        CURSOR.execute(query, values)
        CONN.commit()

    @classmethod
    def find_by_title(cls, title):
        query = "SELECT * FROM songs WHERE title = ?"
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

# Example usage
if __name__ == '__main__':
    # Create a Song object and save it to the database
    song = Song(title="Example Song", artist="Example Artist", album="Example Album")
    song.save()

    # Update the song in the database
    song.artist = "New Artist"
    song.album = "New Album"
    song.update()

    # Find a song by title
    found_song = Song.find_by_title("Example Song")
    if found_song:
        print(f"Found song: {found_song.title} by {found_song.artist}")

    # Retrieve all songs from the database
    all_songs = Song.all()
    for s in all_songs:
        print(f"Song: {s.title} by {s.artist}, Album: {s.album}")
