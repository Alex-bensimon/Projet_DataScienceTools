# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:51:11 2020

@author: Alex le BOSS du Game
"""

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error as MSE
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import make_regression
import numpy as np
import fonction_traitement as trait
import actors_labelisation as act
import pandas as pd
import statistics 
from sklearn.linear_model import LinearRegression,LogisticRegression


def Regression(prediction,movie_ratings, v, ge1,ge2, ge3,osc,rt,budg):
    '''
    Regression code which launch LinearRegression or DecisionTreeRegressor depending
    of the parameter prediction. It will return an IMDB rating, MSE and RMSE score. 
    
    :param1 int prediction: variable used to choose between LinearRegression and DecisionTreeRegressor
    :param2 dataframe movie_ratings: dataframe with all the dataframe from movies
    :param3 int v: number of votes entered in launch_prediction
    :param4 String ge1: fist genre entered in launch_prediction
    :param5 String ge2: second genre entered in launch_prediction
    :param6 String ge3: third genre entered in launch_prediction
    :param7 int osc: number of oscars entered in launch_prediction
    :param8 int rt: runtime of the movie entered in launch_prediction
    :param9 int budg: budget of the movie entered in launch_prediction
    :return void:
    '''

    g1 = act.return_genre_label(ge1)
    g2 = act.return_genre_label(ge2)
    g3 = act.return_genre_label(ge3)
    
    if prediction == "1":
        print("\nGo faire une bonne regression lineaire !!")
        lr = LinearRegression()
    elif prediction == "2":
        print("\nGo faire un arbre de decision !!")
        lr = DecisionTreeRegressor()
    
    X = movie_ratings.drop(["imdb_ratings"],axis=1)
    y = movie_ratings['imdb_ratings']

    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=21)
    
    lr.fit(X_train, y_train)
    
    def deter(lr,votes=v, genre1=g1,genre2=g2,genre3=g3,
               oscars=osc,runtime=rt,budget=budg):
      x = np.array([votes, genre1, genre2,genre3,oscars,
                    runtime,budget]).reshape(1, 7)
      print("\nPrédiction de la note IMDB : ")
      print(lr.predict(x))
    
    deter(lr)
    
    y_pred_lr = lr.predict(X_test)
        
    mse_lr = MSE(y_pred_lr,y_test)
    
    rmse_lr = mse_lr**(1/2)
    
    print('MSE : {:.2f}'.format(mse_lr))
    print('RMSE : {:.2f}'.format(rmse_lr))
    
    
    
def launch_prediction():
    '''
    Script allowed to choose parameters for the Regression function as number of votes, 
    budget, etc ... 
    :return void:
    '''
    
    corres_genres = pd.read_csv(r'correspondances_genres.csv')
    
    movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_1980_2020_final.csv')

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
    print("\nMaintenant, tu vas entrer les caractéristiques d'un film afin de prédire sa note sur le site IMDB :")
    #print("Note moyenne des critiques de cinéma -57/100 en moyenne- : ")
    #metascore = input()

    print("Nombre de votes par le public - 54k en moyenne - : ")
    votes = int(input())

    test_genre1 = False
    while test_genre1 == False:
        print("Genre du film (1/3) - en anglais - : ")
        genre1 = input()
        test = corres_genres['index'] [ corres_genres.genres == genre1].values
        if len(test)!=0:
            test_genre1 = True

    test_genre2 = False
    while test_genre2 == False:
        print("Genre du film (2/3) - en anglais - : ")
        genre2 = input()
        test = corres_genres['index'] [ corres_genres.genres == genre2].values
        if len(test)!=0:
            test_genre2 = True
    
    test_genre3 = False
    while test_genre3 == False:
        print("Genre du film (3/3) - en anglais - : ")
        genre3 = input()
        test = corres_genres['index'] [ corres_genres.genres == genre3].values
        if len(test)!=0:
            test_genre3 = True
    
    print("Nombre d'oscars qu'il mérite de remporter - évite d'en mettre 15... il y en a 0,3 en moy - : ")
    oscars = int(input())
    print("Durée du film - en minutes, moyenne = 103min - : ")
    runtime = int(input())
    print("Budget pour ce chef d'oeuvre - 44M$ en moyenne - : ")
    budget = int(input())
    
    
    if algo == "1" or "2":
        Regression(algo,movie_ratings, votes, genre1,genre2, genre3,oscars,runtime,budget)
    else:
        print("Tu forces, mets un nombre correct...")
        




# Permet de sélectionner les meilleures features mais ne fonctionne pas très bien
"""
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error as MSE
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import make_regression
import numpy as np
import fonction_traitement as trait
import actors_labelisation as act
import pandas as pd
import statistics 
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.feature_selection import SelectKBest, chi2

corres_genres = pd.read_csv(r'correspondances_genres.csv')


movie_ratings = trait.clean_dataframe(movie_ratings,3,4,5,6,7,8)
    
movie_ratings = movie_ratings.drop(["stars1"],axis=1)
movie_ratings = movie_ratings.drop(["stars2"],axis=1)
movie_ratings = movie_ratings.drop(["stars3"],axis=1)
movie_ratings = movie_ratings.drop(["metascore"],axis=1)
movie_ratings = movie_ratings.drop(["win"],axis=1)
movie_ratings = movie_ratings.drop(["nom"],axis=1)
movie_ratings = movie_ratings.drop(["gross"],axis=1)

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']

lab_enc = preprocessing.LabelEncoder()
y_enc = lab_enc.fit_transform(y)

chi2(X, y_enc)

selector = SelectKBest(chi2, k=4)
print(selector.fit(X, y_enc))
print(selector.scores_)

print(np.array(movie_ratings.feature_names)[selector.get_support()])
"""