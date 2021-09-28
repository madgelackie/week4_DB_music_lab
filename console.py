import pdb
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Meatloaf")
artist_repository.save(artist_1)

artist_2 = Artist("Madonna")
artist_repository.save(artist_2)

album_1 = Album("Bat Out of Hell", artist_1, "rock", "1977")
album_repository.save(album_1)

album_2 = Album("Dead Ringer", artist_1, "rock", "1981")
album_repository.save(album_2)

album_3 = Album("True Blue", artist_2, "pop", "1986")
album_repository.save(album_3)

# artist_repository.select(26)

print(artist_repository.select_all())


pdb.set_trace()