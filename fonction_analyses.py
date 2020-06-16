# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:39 2020

@author: Victor HENRIO
"""
import pandas as pd

def data_frame_netoyage(names,years,imdb_ratings,metascores,votes,categories,mv_pages):
    '''
    Create a new dataFrame with all the inforamtion about the movie from the scraping
    
    :param1 list names: list of the name film
    :param2 list years: list of the year film
    :param3 list imdb_ratings: list of score given by imdb for the movie
    :param4 list metascores: liste of metascores of the given film
    :param5 list votes : list of number of votes by movie 
    :return: A pandas Dataframe with all the informations about the movies
    :rtype: pandas.dataframe
    
    '''
    
    
    movie_ratings = pd.DataFrame({
        'movie': names,
        'year': years,
        'imdb': imdb_ratings,
        'metascore': metascores,
        'votes': votes,
        'categories':categories,
        'mv_pages':mv_pages
    })
    
    print(movie_ratings.info())
    
    movie_ratings.head(10)
    
    movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
    
    movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
    
    3
    
    print(movie_ratings.head(10))
    
    return movie_ratings

