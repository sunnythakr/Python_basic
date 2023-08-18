# MusicPlayer class in Python, which models a simple music player:
class Song:
    def __init__(self, title, artist, duration):
        self._title = title  # Encapsulated attribute
        self._artist = artist  # Encapsulated attribute
        self._duration = duration  # Encapsulated attribute

    def play(self):
        print(f"Now playing: {self._title} by {self._artist}")
        print(f"Duration: {self._duration} seconds")


class Playlist:
    def __init__(self, name):
        self._name = name  # Encapsulated attribute
        self._songs = []  # Encapsulated attribute for playlist songs

    def add_song(self, song):
        self._songs.append(song)
        print(f"Added '{song._title}' to the playlist '{self._name}'")

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
            print(f"Removed '{song._title}' from the playlist '{self._name}'")
        else:
            print(f"'{song._title}' not found in the playlist '{self._name}'")

    def play_all(self):
        print(f"Playing all songs in the playlist '{self._name}':")
        for song in self._songs:
            song.play()
            print("---")
        print("End of playlist.")


class MusicPlayer:
    def __init__(self):
        self._playlists = {}  # Encapsulated attribute for playlists

    def create_playlist(self, name):
        self._playlists[name] = Playlist(name)
        print(f"Created playlist '{name}'")

    def get_playlist(self, name):
        return self._playlists.get(name)

    def display_playlists(self):
        print("Playlists:")
        for name, playlist in self._playlists.items():
            print(name)

    def display_playlist_songs(self, name):
        playlist = self._playlists.get(name)
        if playlist:
            print(f"Songs in the playlist '{name}':")
            for song in playlist._songs:
                print(f"{song._title} by {song._artist}")
        else:
            print(f"Playlist '{name}' not found")


# Creating instances of the Song, Playlist, and MusicPlayer classes
song1 = Song("Shape of You", "Ed Sheeran", 233)
song2 = Song("Uptown Funk", "Mark Ronson ft. Bruno Mars", 271)
song3 = Song("Billie Jean", "Michael Jackson", 292)

player = MusicPlayer()

# Using encapsulated methods to interact with the objects
player.create_playlist("Top Hits")
player.create_playlist("Favorites")

top_hits_playlist = player.get_playlist("Top Hits")
favorites_playlist = player.get_playlist("Favorites")

top_hits_playlist.add_song(song1)
top_hits_playlist.add_song(song2)

favorites_playlist.add_song(song2)
favorites_playlist.add_song(song3)

player.display_playlists()

player.display_playlist_songs("Top Hits")
player.display_playlist_songs("Favorites")

favorites_playlist.remove_song(song2)

player.display_playlist_songs("Favorites")

top_hits_playlist.play_all()
