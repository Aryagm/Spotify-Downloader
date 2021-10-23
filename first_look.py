import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="03837d09dbcd49c5b1657f8eb61875d3",
                                                           client_secret="bd86168e23394850b0911987dfec807f"))

def get_song(query:str):
    results = sp.search(q=query, limit=1)
    song_name = results['tracks']['items'][0]['name']
    song_url = results['tracks']['items'][0]['external_urls']['spotify']
    album_name = results['tracks']['items'][0]['album']['name']
    song_image = results['tracks']['items'][0]['album']['images'][0]['url']
    artist_name = results['tracks']['items'][0]['album']['artists'][0]['name']
    return [song_name, song_url, album_name, song_image, artist_name]
