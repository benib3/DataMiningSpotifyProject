from numpy import maximum
import pandas
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time


    
cid='05bf72dc1e11495a8d4a81f6c1663c6e'
secret='eb31cc5997cb4f85bdddab4d6271d495'
#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#playlist_link = "https://open.spotify.com/playlist/4kURMtq9rYBUmp23t0VpUt?si=c634c241a8ce46bf"
#playlist_URI = playlist_link.split("/")[-1].split("?")[0]
#track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]



def getIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids   


def getTrackFeatures(id):
  meta = sp.track(id)
  id_meta_artist=meta['album']['artists'][0]['uri']
  features = sp.audio_features(id)
  artist_id=sp.artist(id_meta_artist)
  
  
  #meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  artist_genre =artist_id['genres']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  

  features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']

 
  

  track = [name, album, artist,artist_genre, release_date, length, acousticness, danceability, energy, instrumentalness, 
           liveness, loudness, speechiness, tempo,]#genre
  return track




ids=getIDs("Roshi","3nZAmcfvxCNBTKB0mz7Hgc")


tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

print(tracks)


df = pandas.DataFrame(tracks, columns = ['name', 'album', 'artist','artist_genre', 'release_date', 'length', 'danceability',
                                           'acousticness',  'energy', 'instrumentalness', 
                                           'liveness', 'loudness', 'speechiness', 'tempo'])
df.to_csv("mojSpotify.csv", sep = ',')