# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:39 2020
@author: Victor HENRIO
"""
import pandas as pd
import math


#def data_frame_netoyage(names,years,imdb_ratings,metascores,votes,categories,mv_pages):
def data_frame_netoyage(mv_attributs):
    '''
    Create a new dataFrame with all the inforamtion about the movie from the scraping

    :param tupe mv_attributs: tupe of all the data frome movies
    :return: A pandas Dataframe with all the informations about the movies
    :rtype: pandas.dataframe

    '''

    movie_ratings = pd.DataFrame({
        'movie': mv_attributs[0],
        'year': mv_attributs[1],
        'imdb_ratings': mv_attributs[2],
        'metascore': mv_attributs[3],
        'votes': mv_attributs[4],
        'category': mv_attributs[5],
        'mv_page': mv_attributs[6],
        'genres' : mv_attributs[7],
        'stars' : mv_attributs[8],
        'rank' : mv_attributs[9],
        'nb_oscar' : mv_attributs[10],
        'win' : mv_attributs[11],
        'nom' : mv_attributs[12],
        'runtime' : mv_attributs[13],
        'budget' : mv_attributs[14],
        'gross' : mv_attributs[15]
    })
    
    movie_ratings.loc[:, 'year'] = movie_ratings['year'].astype(int)
    movie_ratings['n_imdb'] = movie_ratings['imdb_ratings'] * 10   
    
    return movie_ratings


def delete_nan(movie_ratings):
    '''
    '''

    i = 0
    for note in movie_ratings.itertuples():
        test = math.isnan(float(note.n_imdb))
        if test is True:
            movie_ratings = movie_ratings.drop(movie_ratings.index[i])
            i -= 1
        i += 1
    return movie_ratings


def replace_metascore(movie_ratings):
    '''
    '''
    i = 0
    for note in movie_ratings.itertuples():
        test = math.isnan(float(note.metascore))
        if test is True:
            print(movie_ratings['metascore'][i])
            print(note.n_imdb)
            movie_ratings['metascore'] = movie_ratings['metascore'].replace(movie_ratings['metascore'][i], note.n_imdb)
        i += 1
    return movie_ratings


def clean_dataframe(movie_ratings):
    '''
    '''
    
    movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
    movie_ratings = movie_ratings.drop(["imdb_ratings"],axis=1)
    movie_ratings = movie_ratings.set_index('movie')
    movie_ratings['category'] = movie_ratings['category'].replace(regex={'R': '1','PG-13': '3', 'PG': '2'})
    movie_ratings = delete_nan(movie_ratings)
    movie_ratings = replace_metascore(movie_ratings)

    return movie_ratings