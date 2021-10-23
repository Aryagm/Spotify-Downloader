import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

def get_song(query:str):
    results = sp.search(q=query, limit=1)
    song_name = results['tracks']['items'][0]['name']
    song_url = results['tracks']['items'][0]['external_urls']['spotify']
    album_name = results['tracks']['items'][0]['album']['name']
    song_image = results['tracks']['items'][0]['album']['images'][0]['url']
    artist_name = results['tracks']['items'][0]['album']['artists'][0]['name']
    return [song_name, song_url, album_name, song_image, artist_name]
