# Service script to export Spotify playlists and saved songs

import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Loading .env file for Spotify API credentials
load_dotenv()

# Setting up Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id = os.getenv("CLIENT_ID"),
        client_secret = os.getenv("CLIENT_SECRET"),
        redirect_uri = os.getenv("REDIRECT_URI"),
        scope='playlist-read-private user-library-read'))


# Gets the user's saved tracks and returns a list of strings with the format "artist - song"
def get_saved_tracks():

    offset = 0
    counter = 0
    songs_to_save = []

    # Using a while loop and offset to pass the Spotifys maximum limit of 50 songs per request
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

            counter += 1
            print( str(counter) + ". "+ "Fetched name:", artist_song)

    print("Total fetched song names:", len(songs_to_save))

    return songs_to_save

# Gets the user's playlist by a name and returns a list of strings with the format "artist - song"
def get_playlist_tracks(wanted_list):

    offset = 0
    songs_to_save = []

    if not wanted_list:
        print("No playlist name was given")
        return songs_to_save

    playlists = sp.current_user_playlists()

    if len(playlists['items']) == 0:
        print("No playlists were found")
        return songs_to_save

    for playlist in playlists['items']:
        if playlist["name"] == wanted_list:
            playlist_id = playlist["id"]

            # Using a while loop and offset to pass the Spotifys maximum limit of 50 songs per request
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