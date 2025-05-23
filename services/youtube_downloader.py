# Service script to download songs from YouTube

import re
import os
import yt_dlp

# Makes sure that Windows can handle the file names
def refactor_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

# Downloads a song from YouTube and saves it as an MP3 file in the 'songs' directory
def download_song(url, song_name):

    final_name = os.path.join('songs', refactor_filename(song_name) + '.mp3')

    if os.path.exists(final_name):
        print(song_name + " already exists. Skipping download.")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join('songs', 'temp.%(ext)s'),
        "noplaylist": True,
        'no_warnings': True,
        'cookiefile': 'cookies/cookies.txt',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Removes temporary files after the download is done
    for ext in ["webm", "m4a"]:
        temp_path = os.path.join('songs', f'temp.{ext}')
        if os.path.exists(temp_path):
            os.remove(temp_path)

    temp_name = os.path.join('songs', 'temp.mp3')

    # Rename the temporary file and check for duplicates
    if os.path.exists(temp_name):
        os.rename(temp_name, final_name)