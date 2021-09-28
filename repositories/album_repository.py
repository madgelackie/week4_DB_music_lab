from pdb import run
from db.run_sql import run_sql
import repositories.artist_repository as artist_repository
from models.album import Album


def save(album):
    sql = f"INSERT INTO albums (title, artist_id, genre, year) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre, album.year]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums;"
    run_sql(sql)

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist, row['genre'], row['year'], row['id'])