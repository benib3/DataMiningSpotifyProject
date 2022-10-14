from matplotlib.font_manager import json_load
import pandas as pd # import
import numpy as np
from ast import literal_eval
import json
df = pd.read_csv("./mojSpotify.csv",encoding='cp1252') # ucitavanje csv fajla
print("-------------------------------")
print(df.columns)
print("-------------------------------")
print(df['artist_genre'].value_counts)
#provjerio sam values sve bio kroz for loop i value counts i svaka valuje tj zanr je pripadao hip hop pa sam ih objedinio
df['artist_genre']="Classical"

   
df.to_csv("./mojSpotifyClassical.csv",sep=",")  
    
       

print("-------------------------------")

    

