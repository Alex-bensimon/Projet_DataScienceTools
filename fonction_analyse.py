# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:48:03 2020

@author: Alex
"""

import fonction_scraping_accueil as scrap
import fonction_traitement as trait
import definition_tab as dftab
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression,LogisticRegression
import math


def delete_raws_nan2(movie_ratings):
    '''
    If there is not a specific attribut we delete the ligne cause
    
    :param1 dataframe movie_ratings: with all the dataframe from movies,
    :return dataframe movie_ratings: with all the dataframe from movies
    :rtype: dataframe
    
    '''

    i = 0
    for note in movie_ratings['budget']:
        test = math.isnan(float(movie_ratings['budget'][i]))
        print(test)
        if test is True:
            movie_ratings = movie_ratings.drop(movie_ratings.index[i])
            i -= 1
        i += 1
        
    return movie_ratings


movie_ratings = pd.read_csv('movie_ratings_1980_2000_p10.csv')


movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
movie_ratings = movie_ratings.drop(["year"],axis=1)
movie_ratings = movie_ratings.drop(["Unnamed: 0"],axis=1)
movie_ratings = movie_ratings.drop(["rank"],axis=1)
movie_ratings = movie_ratings.drop(["category"],axis=1)
#movie_ratings = movie_ratings.drop(["genres1"],axis=1)
#movie_ratings = movie_ratings.drop(["genres2"],axis=1)
#movie_ratings = movie_ratings.drop(["genres3"],axis=1)
movie_ratings = movie_ratings.drop(["stars1"],axis=1)
movie_ratings = movie_ratings.drop(["stars2"],axis=1)
movie_ratings = movie_ratings.drop(["stars3"],axis=1)
movie_ratings = movie_ratings.set_index('movie')
#movie_ratings['category'] = movie_ratings['category'].replace(regex={'R': '1','PG-13': '3', 'PG': '2'})
movie_ratings['runtime']=movie_ratings['runtime'].fillna(movie_ratings['runtime'].mean())

movie_ratings = trait.delete_raws_nan(movie_ratings)
#movie_ratings = trait.replace_metascore(movie_ratings)
#movie_ratings = delete_raws_nan2(movie_ratings)

moy_genre = []
genre = "Adventure"
# making boolean series for a team name 
filter = str(movie_ratings["genres1"])==genre
  
i = 0
#for budget in movie_ratings['budget']:
moy_genre = movie_ratings['budget'].where(filter, inplace = True) 

print(moy_genre)
print("---"*30)
print(movie_ratings.info())
print(movie_ratings['budget'].tail(50))

"""
X = movie_ratings
X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings["imdb_ratings"]

model = LinearRegression()
model.fit(X, y) # entrainement du modele
model.score(X, y) # évaluation avec le coefficient de corrélation
plt.scatter(X, y)
plt.plot(X, model.predict(X), c='red')

model1 = LogisticRegression()
model1.fit(X, y) # entrainement du modele
model1.score(X, y) # évaluation avec le coefficient de corrélation
plt.scatter(X, y)
plt.plot(X, model1.predict(X), c='red')
"""
