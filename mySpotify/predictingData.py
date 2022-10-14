import pickle
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing


df=pd.read_csv("./mojSpotifyBezZanrovi.csv")
data=pd.DataFrame(df,columns=['acousticness', 'danceability', 'energy',
       'instrumentalness', 'loudness', 
       'speechiness', 'tempo','genre'])


zavisne=['acousticness', 'danceability', 'energy',
       'instrumentalness', 'loudness', 
       'speechiness', 'tempo']

loaded_model = pickle.load(open('gnb_final_model.sav', 'rb'))

pred = loaded_model.predict(data[zavisne])#

print("-------------------------------")
print("Naive Bayes")
print(pred)
data['genre'] = pred
data.to_csv('mojSpotifyPredZanrovi.csv')

print("-------------------------------")
    