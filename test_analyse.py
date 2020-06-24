# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:51:11 2020

@author: Alex
"""
import fonction_traitement as trait
import actors_labelisation as act
import pandas as pd
import statistics 
import API as api

movie_ratings = pd.read_csv(r'Data_csv\test_csv.csv')

#movie_ratings = api.API_search_director(movie_ratings)

movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
movie_ratings = movie_ratings.drop(["year"],axis=1)
movie_ratings = movie_ratings.drop(["Unnamed: 0"],axis=1)
movie_ratings = movie_ratings.drop(["rank"],axis=1)
movie_ratings = movie_ratings.drop(["category"],axis=1)
movie_ratings = movie_ratings.set_index('movie')
movie_ratings['runtime'] = movie_ratings['runtime'].fillna(movie_ratings['runtime'].mean())
movie_ratings = trait.replace_metascore(movie_ratings)
movie_ratings = trait.add_0_win_nom(movie_ratings)
movie_ratings['budget'] = movie_ratings['budget'].fillna(movie_ratings['budget'].mean())
movie_ratings['gross'] = movie_ratings['gross'].fillna(movie_ratings['gross'].mean())

movie_ratings = act.imputation_previous_value(movie_ratings)
movie_ratings = movie_ratings.dropna()
movie_ratings = act.labelisation(movie_ratings)



print(movie_ratings.info())

#%%

import fonction_traitement as trait
import actors_labelisation as act
import pandas as pd
import statistics 
import API as api
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn import preprocessing
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.linear_model import LinearRegression,LogisticRegression



movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')

#movie_ratings = api.API_search_director(movie_ratings)

movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
movie_ratings = movie_ratings.drop(["year"],axis=1)
movie_ratings = movie_ratings.drop(["Unnamed: 0"],axis=1)
movie_ratings = movie_ratings.drop(["rank"],axis=1)
movie_ratings = movie_ratings.drop(["category"],axis=1)
movie_ratings = movie_ratings.set_index('movie')
movie_ratings['runtime'] = movie_ratings['runtime'].fillna(movie_ratings['runtime'].mean())
movie_ratings = trait.replace_metascore(movie_ratings)
movie_ratings = trait.add_0_win_nom(movie_ratings)
movie_ratings['budget'] = movie_ratings['budget'].fillna(movie_ratings['budget'].mean())
movie_ratings['gross'] = movie_ratings['gross'].fillna(movie_ratings['gross'].mean())

movie_ratings = act.imputation_previous_value(movie_ratings)
movie_ratings = movie_ratings.dropna()
movie_ratings = act.labelisation(movie_ratings)

movie_ratings = movie_ratings.drop(["stars1"],axis=1)
movie_ratings = movie_ratings.drop(["stars2"],axis=1)
movie_ratings = movie_ratings.drop(["stars3"],axis=1)
movie_ratings = movie_ratings.drop(["metascore"],axis=1)
movie_ratings = movie_ratings.drop(["win"],axis=1)
movie_ratings = movie_ratings.drop(["nom"],axis=1)

print(movie_ratings.info())


#%%

#model = KNeighborsClassifier()
#model = LinearSVC(random_state=0, max_iter=500)
model = LinearRegression()
#model = LogisticRegression()

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
           nb_oscar=0,runtime=123,budget=125000000,gross=546000000):
  x = np.array([votes, genre1, genre2,genre3,nb_oscar,
                runtime,budget,gross]).reshape(1, 8)
  print("Prédiction : ")
  print(model.predict(x))
  #print(model.predict_proba(x))


deter(model)

#%%

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