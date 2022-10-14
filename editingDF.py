import pandas as pd # import
df = pd.read_csv("./SpotifyFeaturesGenre.csv",encoding='cp1252') # ucitavanje csv fajla
print(df['genre'].value_counts())

df1 = df[df['genre']=='Rap'] # 
df2 = df[df['genre']=='Rock'] #
df3 = df[df['genre']=='Jazz'] # 
df4 = df[df['genre']=='Classical'] #
df5 = df[df['genre']=='Reggae'] #
df6 = df[df['genre']=='Dance'] #



df1 = df1.sample(1000) 
df2 = df2.sample(1000) 
df3 = df3.sample(1000) 
df4 = df4.sample(1000) 
df5 = df5.sample(1000) 
df6 = df6.sample(1000) 

pd.concat([
     pd.concat([df1,df2,df3,df4,df5,df6])]).to_csv('noviZanrovi6.csv',index = False, header = True)
