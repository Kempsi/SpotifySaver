from turtle import down
from services.spotify_exporter import get_playlist_tracks, get_saved_tracks
from services.youtube_searcher import get_youtube_url
from services.youtube_downloader import download_song 

def save_all_songs():

    songs = get_saved_tracks()

    for song in songs:
        url = get_youtube_url(song + " audio")
        print("Query: " + song + " - audio")

        if (url is not None):
            download_song(url, song)


def save_playlist(playlist_name):

    songs = get_playlist_tracks(playlist_name)

    for song in songs:
        url = get_youtube_url(song + " audio")
        print("Query: " + song + " - audio")

        if (url is not None):
            download_song(url, song)


save_playlist("Pendulum")
















