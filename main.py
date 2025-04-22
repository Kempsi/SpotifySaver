# Main script to save songs from Spotify locally using YouTube as a tool

from services.spotify_exporter import get_playlist_tracks, get_saved_tracks
from services.youtube_searcher import get_youtube_url
from services.youtube_downloader import download_song 

# Saves all the liked songs from the user's Spotify account
def save_all_songs():

    songs = get_saved_tracks()

    if len(songs) == 0:
        print("No songs found!")
        return

    for song in songs:
        url = get_youtube_url(song + " audio")
        print("Query: " + song + " - audio")

        if (url is not None):
            download_song(url, song)


# Saves all the songs from a specific playlist
def save_playlist(playlist_name):

    songs = get_playlist_tracks(playlist_name)

    if len(songs) == 0:
        print("No songs found!")
        return

    for song in songs:
        url = get_youtube_url(song + " audio")
        print("Query: " + song + " - audio")

        if (url is not None):
            download_song(url, song)

# save_playlist("Pendulum")
save_all_songs()