import yt_dlp

def get_youtube_url(query : str):
    yt_dlp_opts = {
        "quiet": True,
        "skip_download": True,
        "default_search": "ytsearch",
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
        results = ydl.extract_info(query, download=False)
        if "entries" in results and results["entries"]:
            video = results["entries"][0]
            return video.get("webpage_url")
        else:   
            return None

