# Library of songs  of different movies.
# Each movie can have more than one song
# Each song is sung by one artist
# Each song in a movie can be of different genre
#
# Search songs based on Artist name or  movie name or Genre name

class Artist:
    pass


class Movie:
    pass


class Genre(Enum):
    pass


class Song:
    movie: Movie  # ForeignKey
    genre: Genre  # Choice
    artists: Artist  # M2M with through SongArtist


class SongArtist:
    song: Song  # ForeignKey
    artist: Artist  # SongArtist
