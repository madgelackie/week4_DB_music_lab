from pdb import run
from db.run_sql import run_sql
import repositories.artist_repository as artist_repository
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, genre, year) VALUES (%s, %s, %s) RETURNING * "
    values = [album.title, album.genre, album.year]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album