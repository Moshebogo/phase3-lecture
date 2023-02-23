import sqlite3
import pprint

connection = sqlite3.connect('chinook.db')
cursor = connection.execute("select * from albums where AlbumId <= 100")

class Album:
    def __init__(self, albumId, title, artistId):
        self.albumId = albumId
        self.title = title
        self.artisId = artistId

result = cursor.fetchall()
