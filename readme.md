# SpotifySaver

TL;DR: SpotifySaver is a script that allows you to download your Spotify playlists and 
saved tracks using YouTube, directly to your computer for offline listening.

### Overview
SpotifySaver connects to the Spotify Web API to retrieve track data, and uses YouTube as the source for downloading corresponding audio files. 
It relies on user authentication via Spotify’s Developer portal and performs the following steps in sequence:

### Authentication
A developer application must be created at developer.spotify.com.
The client ID and client secret from the app are used to authenticate the user.
Upon successful authentication, a .cache file is generated. 
This file contains an access token that is automatically used for future requests.

### Playlist Sources
The script currently supports two types of sources:
- A specific playlist by name
- The user's saved (Liked) tracks

### Process Flow
1. Fetch all track names and corresponding artists using the format:
"Artist - Track Name"
2. Append the keyword "audio" to each search query.
3. Perform a YouTube search using the full query and select the first result.
4. Retrieve the video URL from the search result.
5. Download the video’s audio in .mp3 format using yt-dlp and save it locally.
