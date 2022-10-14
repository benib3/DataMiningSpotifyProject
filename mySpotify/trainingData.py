import pickle
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
df=pd.read_csv("./editGenre.csv")
data=pd.DataFrame(df,columns=['acousticness', 'danceability', 'energy',
       'instrumentalness', 'loudness', 
       'speechiness', 'tempo','genre'])

#data["genre"]=preprocessing.LabelEncoder().fit_transform(data["genre"])
# for i in data.genre.values:
#     if i=="Hip-Hop":
#          data.genre.replace(i, 0, inplace = True)
#     elif i=="Rock":
#          data.genre.replace(i, 1, inplace = True)
#     elif i=="Classical":
#            data.genre.replace(i,2,inplace=True)
#     elif i=="Jazz":
#            data.genre.replace(i,3,inplace=True)
print("-------------------------------")

zavisne=['acousticness', 'danceability', 'energy',
       'instrumentalness', 'loudness', 
       'speechiness', 'tempo']
print(data['genre'].values)

print(data.head(5))
print(data.info)
print(data.dtypes)

X=data[zavisne].values
y=data['genre'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=1)

# for col in zavisne :
#         plt.figure(figsize=[10,5])
#         sns.histplot(df[col])
# plt.figure(figsize=[10,5])
# sns.histplot(df['genre'])
# plt.show()

gnb = GaussianNB()
# #Train the model using the training sets
gnb.fit(X_train, y_train)

filename = 'gnb_final_model.sav'
pickle.dump(gnb, open(filename, 'wb'))


# #Predict the response for test dataset
y_pred = gnb.predict(X_test)
print(y_pred)
print("-------------------------------")
print("Naive Bayes")
print(f"Training: {gnb.score(X_train, y_train)}")
print(f"Test: {gnb.score(X_test, y_test)}")
print("-------------------------------")
print(f'Model accuracy score: {100*accuracy_score(y_test, y_pred):0.2f}%')

cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix')
print(cm)


