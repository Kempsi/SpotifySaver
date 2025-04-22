import os
import yt_dlp


def download_song(url, song_name):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join('songs', 'temp.%(ext)s'),
        "noplaylist": True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for ext in ["webm", "m4a"]:
        temp_path = os.path.join('songs', f'temp.{ext}')
        if os.path.exists(temp_path):
            os.remove(temp_path)

    temp_mp3 = os.path.join('songs', 'temp.mp3')
    final_path = os.path.join('songs', f'{song_name}.mp3')

    if os.path.exists(temp_mp3):
    
        if os.path.exists(final_path):
            os.remove(final_path)

        os.rename(temp_mp3, final_path)
          
