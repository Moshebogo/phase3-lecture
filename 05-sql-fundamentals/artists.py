import sqlite3

connection = sqlite3.connect('chinook.db')
cursor = connection.cursor()

class Artist():
    def __init__(self, artistId, name):
        self.artistId = artistId
        self.name = name

def add_artist(self, name):
    sql = f"""
    INSERT INTO artists
    VALUE {(name)}
    """
    cursor.execute(sql)
    connection.commit()

def get_all_artists(self):
    sql = f"""
    SELECT * 
    FROM artists
    """
    cursor.execute(sql)
    connection.commit()


if __name__ == '__main__':
    pass