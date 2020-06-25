# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:51:11 2020

@author: Alex le BOSS du Game
"""

import fonction_traitement as trait
import actors_labelisation as act
import pandas as pd
import statistics 
import API as api
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.linear_model import LinearRegression,LogisticRegression


movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')

movie_ratings = trait.clean_dataframe(movie_ratings,3,4,5,6,7,8)

#movie_ratings = movie_ratings.drop(["stars1"],axis=1)
movie_ratings = movie_ratings.drop(["stars2"],axis=1)
movie_ratings = movie_ratings.drop(["stars3"],axis=1)
movie_ratings = movie_ratings.drop(["votes"],axis=1)
movie_ratings = movie_ratings.drop(["metascore"],axis=1)
movie_ratings = movie_ratings.drop(["win"],axis=1)
movie_ratings = movie_ratings.drop(["nom"],axis=1)
movie_ratings = movie_ratings.drop(["nb_oscar"],axis=1)
movie_ratings = movie_ratings.drop(["gross"],axis=1)

"""
print the genre's label
"""

genre = 'Drama'
stars = 'Bradley Cooper'
print(act.return_genre_label(genre))
print(act.return_star_label(stars))

print(movie_ratings.info())


#%%

def launch_prediction(movie_ratings):
    
    print('###### ATTENTION : la prédiction va commencer ######\n')
    print("---"*25)
    print("Quel algorithme veux-tu choisir (taper 1 ou 2) : "
          +"\n1. Linear Regression \n2. Decision Tree Regressor ")
    algo = input()
    print('Tu as chosisi : ' + algo)
    print("\n Maintenant, tu vas entrer les caractéristiques d'un film afin de prédire sa note sur le site IMDB :")

    if algo == 1:
        pass
    elif algo == 2:
        pass
    else:
        print("Tu forces, mets un nombre correct...")
    
launch_prediction()



#%%
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error as MSE
from sklearn.tree import DecisionTreeRegressor

#lr = LinearRegression()
lr = DecisionTreeRegressor(max_depth=8,min_samples_leaf=0.1, random_state=2)


X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']

"""
Add algo qui sélectionne les features qui influent le +
"""

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=21)

lr.fit(X_train, y_train)

def deter(lr,votes=181000, genre1=0,genre2=4,genre3=5,
           nb_oscar=0,runtime=109,budget=45000000,gross=212000000):
  x = np.array([votes, genre1, genre2,genre3,nb_oscar,
                runtime,budget,gross]).reshape(1, 8)
  print("Prédiction : ")
  print(lr.predict(x))
  #print(model.predict_proba(x))

deter(lr)

y_pred_lr = lr.predict(X_test)

print(y_pred_lr)

mse_lr = MSE(y_pred_lr,y_test)

rmse_lr = mse_lr**(1/2)

print('MSE lr : {:.2f}'.format(mse_lr))
print('RMSE lr : {:.2f}'.format(rmse_lr))

#%%
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error as MSE
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import make_regression

ge1 = 'Action'
ge2 = 'Comedy'
ge3 = 'Crime'

st1 = 'Brad Pitt'
st2 = 'Michael Caine'
st3 = 'Benjamin Bratt'

g1 = act.return_genre_label(ge1)
g2 = act.return_genre_label(ge2)
g3 = act.return_genre_label(ge3)

s1 = act.return_star_label(st1)
#s2 = act.return_star_label(st2)
#s3 = act.return_star_label(st3)

#lr = LinearRegression()
lr = DecisionTreeRegressor(max_depth=8,min_samples_leaf=0.1, random_state=2)

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']


"""
Add algo qui sélectionne les features qui influent le +
"""

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=21)

lr.fit(X_train, y_train)

def deter(lr, genre1=g1,genre2=g2,genre3=g3,stars1=s1,
           runtime=109,budget=45000000):
  x = np.array([genre1, genre2,genre3,stars1,
                runtime,budget]).reshape(1, 6)
  print("Prédiction : ")
  print(lr.predict(x))
  #print(model.predict_proba(x))

deter(lr)

y_pred_lr = lr.predict(X_test)

print(y_pred_lr)

mse_lr = MSE(y_pred_lr,y_test)

rmse_lr = mse_lr**(1/2)

print('MSE lr : {:.2f}'.format(mse_lr))
print('RMSE lr : {:.2f}'.format(rmse_lr))


#%%

model = LinearRegression()

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']

lab_enc = preprocessing.LabelEncoder()
y_enc = lab_enc.fit_transform(y)

model.fit(X, y_enc) # entrainement du modele
print(model.score(X, y_enc)) # évaluation

"""
Add algo qui sélectionne les features qui influent le +
"""

def deter(model,votes=305000, genre1=0,genre2=1,genre3=2,
           nb_oscar=0,runtime=123,budget=125000000):
  x = np.array([votes, genre1, genre2,genre3,nb_oscar,
             runtime,budget]).reshape(1, 7)
  print("Prédiction : ")
  print(model.predict(x))
  #print(model.predict_proba(x))


deter(model)

#%%

from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_regression

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']

lab_enc = preprocessing.LabelEncoder()
y_enc = lab_enc.fit_transform(y)

model.fit(X, y_enc) # entrainement du modele
print(model.score(X, y_enc)) # évaluation

X, y_enc = make_regression(n_features=2, random_state=0)
regr = ElasticNet(random_state=0)
regr.fit(X, y_enc)

model = ElasticNet(random_state=0)
print(regr.coef_)
print(regr.intercept_)
print(regr.predict([[0, 0]]))

#%%

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error as MSE

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']
"""
lab_enc = preprocessing.LabelEncoder()
y_enc = lab_enc.fit_transform(y)
"""
#model.fit(X, y) # entrainement du modele
#print(model.score(X, y)) # évaluation

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=21)

model = DecisionTreeRegressor(max_depth=8,min_samples_leaf=0.1, random_state=2)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse_dt = MSE(y_pred,y_test)

rmse_dt = mse_dt**(1/2)

print('RMSE dt : {:.2f}'.format(rmse_dt))
"""
X, y = make_regression(n_features=8, n_informative=2,random_state=0, shuffle=False)
regr = RandomForestRegressor(max_depth=6, random_state=0)
regr.fit(X, y)

print(regr.predict([[20, 2, 1, 10,20, 2, 1, 10]]))
"""
#%%

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']

lab_enc = preprocessing.LabelEncoder()
y_enc = lab_enc.fit_transform(y)

chi2(X, y_enc)

selector = SelectKBest(f_classif, k=4)
print(selector.fit(X, y_enc))
print(selector.scores_)

print(np.array(movie_ratings.feature_names)[selector.get_support()])

#%%

budgets = []
"""
genre = "Drama"
filter = movie_ratings["genres1"] == genre
moy_genre = movie_ratings['budget'].where(filter, inplace = True) 
"""
i = 0 
ref = 'Drama'
for c in movie_ratings["genres1"]:
    genre = c
    if genre == ref:
        budgets.append(movie_ratings['budget'][i])
    i += 1
    
print(budgets_propre)
moy_genre = statistics.mean(budgets_propre)
print(moy_genre)

#print(movie_ratings.info())