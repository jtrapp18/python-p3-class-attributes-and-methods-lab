class Song:
    count = 0
    artists = set()
    genres = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        self.add_to_genres()
        self.add_to_artists()

    def add_to_genres(self):
        Song.genres.add(self.genre)

        curr_count = Song.genre_count.get(self.genre, 0)
        print(curr_count)
        Song.genre_count[self.genre] = curr_count + 1

    def add_to_artists(self):
        Song.artists.add(self.artist)

        curr_count = Song.artist_count.get(self.artist, 0)
        Song.artist_count[self.artist] = curr_count + 1


Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Smells Like Teen Spirit", "Nirvana", "Rock")
Song("Out of Touch", "Hall and Oates", "Pop")
Song("Sara Smile", "Hall and Oates", "Pop")

print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)