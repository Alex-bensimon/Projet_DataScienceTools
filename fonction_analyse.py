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

movie_ratings = movie_ratings.drop(["stars1"],axis=1)
movie_ratings = movie_ratings.drop(["stars2"],axis=1)
movie_ratings = movie_ratings.drop(["stars3"],axis=1)
#movie_ratings = movie_ratings.drop(["votes"],axis=1)
movie_ratings = movie_ratings.drop(["metascore"],axis=1)
movie_ratings = movie_ratings.drop(["win"],axis=1)
movie_ratings = movie_ratings.drop(["nom"],axis=1)
#movie_ratings = movie_ratings.drop(["nb_oscar"],axis=1)
#movie_ratings = movie_ratings.drop(["gross"],axis=1)

#movie_ratings = api.API_search_director(movie_ratings)

print(movie_ratings.info())
print(movie_ratings.mean())


#%%
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error as MSE
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import make_regression

def Regression(predict,movie_ratings, v, ge1,ge2, ge3,osc,rt,budg):

    #ge1 = 'Action'
    #ge2 = 'Comedy'
    #ge3 = 'Crime'
    
    #st1 = 'Brad Pitt'
    #st2 = 'Michael Caine'
    #st3 = 'Benjamin Bratt'

    g1 = act.return_genre_label(ge1)
    g2 = act.return_genre_label(ge2)
    g3 = act.return_genre_label(ge3)
    
    #s1 = act.return_star_label(st1)
    #s2 = act.return_star_label(st2)
    #s3 = act.return_star_label(st3)
    
    if predict == "1":
        lr = LinearRegression()
    elif predict == "2":
        lr = DecisionTreeRegressor(max_depth=8,min_samples_leaf=0.1, random_state=2)
    
    X = movie_ratings.drop(["imdb_ratings"],axis=1)
    y = movie_ratings['imdb_ratings']

    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=21)
    
    lr.fit(X_train, y_train)
    
    def deter(lr,votes=v, genre1=g1,genre2=g2,genre3=g3,
               oscars=osc,runtime=rt,budget=budg):
      x = np.array([votes, genre1, genre2,genre3,oscars,
                    runtime,budget]).reshape(1, 7)
      print("Prédiction : ")
      print(lr.predict(x))
      #print(model.predict_proba(x))
    
    deter(lr)
    
    y_pred_lr = lr.predict(X_test)
        
    mse_lr = MSE(y_pred_lr,y_test)
    
    rmse_lr = mse_lr**(1/2)
    
    print('MSE lr : {:.2f}'.format(mse_lr))
    print('RMSE lr : {:.2f}'.format(rmse_lr))
    
    
    
def launch_prediction(movie_ratings):
    
    #movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')

    movie_ratings = trait.clean_dataframe(movie_ratings,3,4,5,6,7,8)
    
    movie_ratings = movie_ratings.drop(["stars1"],axis=1)
    movie_ratings = movie_ratings.drop(["stars2"],axis=1)
    movie_ratings = movie_ratings.drop(["stars3"],axis=1)
    movie_ratings = movie_ratings.drop(["metascore"],axis=1)
    movie_ratings = movie_ratings.drop(["win"],axis=1)
    movie_ratings = movie_ratings.drop(["nom"],axis=1)
    movie_ratings = movie_ratings.drop(["gross"],axis=1)
    
    print('###### ATTENTION : la prédiction va commencer ######\n')
    print("---"*25)
    print("Quel algorithme veux-tu choisir (taper 1 ou 2) : "
          +"\n1. Linear Regression \n2. Decision Tree Regressor ")
    algo = input()
    print('Tu as chosisi : ' + algo)
    print("\n Maintenant, tu vas entrer les caractéristiques d'un film afin de prédire sa note sur le site IMDB :")
    #print("Note moyenne des critiques de cinéma -57/100 en moyenne- : ")
    #metascore = input()
    print("Nombre de votes par le public - 54k en moyenne - : ")
    votes = int(input())
    print("Genre du film (1/3) - en anglais - : ")
    genre1 = input()
    print("Genre du film (2/3) - en anglais - : ")
    genre2 = input()
    print("Genre du film (3/3) - en anglais - : ")
    genre3 = input()
    print("Nombre d'oscars qu'il mérite de remporter -évite d'en mettre 15...-0,3 en moy- : ")
    oscars = int(input())
    print("Durée du film - en minutes, moyenne=103min - : ")
    runtime = int(input())
    print("Budget pour ce chef d'oeuvre - 44M$ en moyenne - : ")
    budget = int(input())
    
    if algo == "1" or "2":
        Regression(algo,movie_ratings, votes, genre1,genre2, genre3,oscars,runtime,budget)
    else:
        print("Tu forces, mets un nombre correct...")
        
movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')
launch_prediction(movie_ratings)




#%%
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error as MSE
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import make_regression


def Linear_Regression(movie_ratings, v, ge1,ge2, ge3,osc,rt,budg):

    #ge1 = 'Action'
    #ge2 = 'Comedy'
    #ge3 = 'Crime'
    
    #st1 = 'Brad Pitt'
    #st2 = 'Michael Caine'
    #st3 = 'Benjamin Bratt'

    g1 = act.return_genre_label(ge1)
    g2 = act.return_genre_label(ge2)
    g3 = act.return_genre_label(ge3)
    
    #s1 = act.return_star_label(st1)
    #s2 = act.return_star_label(st2)
    #s3 = act.return_star_label(st3)
    
    lr = LinearRegression()
    #lr = DecisionTreeRegressor(max_depth=8,min_samples_leaf=0.1, random_state=2)
    
    X = movie_ratings.drop(["imdb_ratings"],axis=1)
    y = movie_ratings['imdb_ratings']

    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=21)
    
    lr.fit(X_train, y_train)
    
    def deter(lr,votes=v, genre1=g1,genre2=g2,genre3=g3,
               oscars=osc,runtime=rt,budget=budg):
      x = np.array([votes, genre1, genre2,genre3,oscars,
                    runtime,budget]).reshape(1, 7)
      print("Prédiction : ")
      print(lr.predict(x))
      #print(model.predict_proba(x))
    
    deter(lr)
    
    y_pred_lr = lr.predict(X_test)
        
    mse_lr = MSE(y_pred_lr,y_test)
    
    rmse_lr = mse_lr**(1/2)
    
    print('MSE lr : {:.2f}'.format(mse_lr))
    print('RMSE lr : {:.2f}'.format(rmse_lr))
    
movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')

movie_ratings = trait.clean_dataframe(movie_ratings,3,4,5,6,7,8)

movie_ratings = movie_ratings.drop(["stars1"],axis=1)
movie_ratings = movie_ratings.drop(["stars2"],axis=1)
movie_ratings = movie_ratings.drop(["stars3"],axis=1)
#movie_ratings = movie_ratings.drop(["votes"],axis=1)
movie_ratings = movie_ratings.drop(["metascore"],axis=1)
movie_ratings = movie_ratings.drop(["win"],axis=1)
movie_ratings = movie_ratings.drop(["nom"],axis=1)
#movie_ratings = movie_ratings.drop(["nb_oscar"],axis=1)
movie_ratings = movie_ratings.drop(["gross"],axis=1)
Linear_Regression(movie_ratings,100000, 'Action','Drama', 'Adventure',0,120,50000000)
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

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']

lab_enc = preprocessing.LabelEncoder()
y_enc = lab_enc.fit_transform(y)

chi2(X, y_enc)

selector = SelectKBest(f_classif, k=4)
print(selector.fit(X, y_enc))
print(selector.scores_)

print(np.array(movie_ratings.feature_names)[selector.get_support()])
