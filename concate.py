# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:18:51 2020

@author: Victor HENRIO
"""

import pandas as pd

movie_ratings_1 = pd.read_csv("./Data_csv/movie_ratings_2020_2016_p25(v2).csv")

movie_ratings_1 = movie_ratings_1.drop(["Unnamed: 0"],axis=1)
movie_ratings_1 = movie_ratings_1.drop(["Column1"],axis=1)
movie_ratings_1.info()
#%%

movie_ratings_2 = pd.read_csv(r'Data_csv\movie_ratings_full.csv')
movie_ratings_2 = movie_ratings_2.drop(["Unnamed: 0"],axis=1)
movie_ratings_2.info()
#%%

movie_ratings = pd.concat([movie_ratings_1,movie_ratings_2])
#%%
movie_ratings.to_csv("movie_ratings_1980_2020_final.csv")
