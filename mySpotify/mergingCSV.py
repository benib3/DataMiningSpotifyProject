import pandas as pd # import
df1 = pd.read_csv("./mojSpotifyHipHop.csv",encoding='cp1252') # ucitavanje csv fajla
df2 = pd.read_csv("./mojSpotifyJazz.csv",encoding='cp1252') # ucitavanje csv fajla
df3 = pd.read_csv("./mojSpotifyClassical.csv",encoding='cp1252') # ucitavanje csv fajla
df4 = pd.read_csv("./mojSpotifyRock.csv",encoding='cp1252') # ucitavanje csv fajla


pd.concat([
     pd.concat([df1,df2,df3,df4])]).to_csv('mojSpotifyZanrovi.csv',index = False, header = True)