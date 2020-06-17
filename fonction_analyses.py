# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:39 2020
@author: Victor HENRIO
"""
import pandas as pd
import math

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
        'imdb_ratings': imdb_ratings,
        'metascore': metascores,
        'votes': votes,
        'category':categories,
        'mv_page':mv_pages
    })
    
    movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
    movie_ratings['n_imdb'] = movie_ratings['imdb_ratings'] * 10   
    
    return movie_ratings

def delete_nan(movie_ratings):
    i = 0
    for note in movie_ratings.itertuples():
        test = math.isnan(float(note.n_imdb))
        if test is True:
            movie_ratings = movie_ratings.drop(movie_ratings.index[i])
            i -= 1
        i += 1
    return movie_ratings
