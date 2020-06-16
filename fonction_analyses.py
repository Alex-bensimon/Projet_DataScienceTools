# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:39 2020

@author: Victor HENRIO
"""
import pandas as pd

def data_frame_netoyage(names,years,imdb_ratings,metascores,votes):
    
    movie_ratings = pd.DataFrame({
        'movie': names,
        'year': years,
        'imdb': imdb_ratings,
        'metascore': metascores,
        'votes': votes  
    })
    
    print(movie_ratings.info())
    
    movie_ratings.head(10)
    
    movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
    
    movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
    
    movie_ratings.to_csv('movie_ratings.csv')
    
    return movie_ratings