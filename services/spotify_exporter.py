import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id = os.getenv("CLIENT_ID"),
        client_secret = os.getenv("CLIENT_SECRET"),
        redirect_uri = os.getenv("REDIRECT_URI"),
        scope='playlist-read-private user-library-read'))


def get_saved_tracks():

    offset = 0
    songs_to_save = []

    while True:

        results = sp.current_user_saved_tracks(offset=offset, limit=50)
        offset += 50

        if len(results['items']) == 0:
            break

        for item in results["items"]:
            track = item['track']
            artist = track['artists'][0]['name']
            track_name = track['name']
            artist_song = f'{artist} - {track_name}'
            songs_to_save.append(artist_song)


    return songs_to_save

def get_playlist_tracks(wanted_list):

    offset = 0
    songs_to_save = []

    playlists = sp.current_user_playlists()

    for playlist in playlists['items']:
        if playlist["name"] == wanted_list:
            playlist_id = playlist["id"]

            
            while True:
            
                results = sp.playlist_tracks(playlist_id, offset=offset, limit=50)
                offset += 50

                
                if len(results['items']) == 0:
                    break

                for song in results["items"]:
                    artist = song['track']['artists'][0]['name']
                    track = song['track']['name']
                    artist_song = f'{artist} - {track}'
                    songs_to_save.append(artist_song)

    return songs_to_save




























