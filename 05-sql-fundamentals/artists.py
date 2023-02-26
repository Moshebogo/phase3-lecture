import sqlite3

connection = sqlite3.connect('chinook.db')
cursor = connection.cursor()

class Artist:
    def __init__(self):
        self.artistId = None
        self.name = None

    def get_artists(self, id1=0, id2=1000):
        sql = f"""
        SELECT * 
        FROM artists
        WHERE ArtistId  BETWEEN  {id1} AND {id2}
        """
        result = cursor.execute(sql).fetchall()
        return result
    
    def add_artist(self, name):
        sql = f"""
        INSERT INTO artists (Name)
        VALUES ('{name}')
        """
        cursor.execute(sql)
        connection.commit()

    def edit_artist(self):
        sql = f"""
        EDIT ***
        """    
        cursor.execute(sql)
        connection.commit()


    def delete_artist(self, name):
        sql = f"""
        DELETE FROM artists 
        WHERE Name LIKE ('{name}')
        """   
        cursor.execute(sql)
        connection.commit()

if __name__ == '__main__':
    print(Artist().get_artists())
    print(Artist().add_artist("Benny Friedman"))
    print(Artist().delete_artist("Benny Friedman"))