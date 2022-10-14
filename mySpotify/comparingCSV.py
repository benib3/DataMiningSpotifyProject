import pandas as pd
from sklearn.metrics import accuracy_score
dataPred=pd.read_csv("./mojSpotifyPredZanrovi.csv")
dfPred=pd.DataFrame(dataPred,columns=['acousticness', 'danceability', 'energy',
       'instrumentalness', 'loudness', 
       'speechiness', 'tempo','genre'])
data=pd.read_csv("./mojSpotifyZanrovi.csv")
df=pd.DataFrame(data,columns=['acousticness', 'danceability', 'energy',
       'instrumentalness', 'loudness', 
       'speechiness', 'tempo','genre'])

x=dfPred['genre'].values
y=df['genre'].values

print(x)
print(y)

print(f'Model accuracy score: {100*accuracy_score(x, y):0.2f}%')