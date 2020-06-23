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

movie_ratings = pd.read_csv('Data_csv\movie_ratings_1980_2000_p10.csv')


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