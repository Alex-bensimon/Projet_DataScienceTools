# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:39 2020
@author: Victor HENRIO
"""

import math
import pandas as pd
import actors_labelisation as act
import pandas as pd
import statistics 
import API as api
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder

def delete_raws_nan(movie_ratings):
    '''
    If there is not a specific attribut we delete the ligne cause
    
    :param1 dataframe movie_ratings: with all the dataframe from movies,
    :return dataframe movie_ratings: with all the dataframe from movies
    :rtype: dataframe
    
    '''

    i = 0
    for note in movie_ratings.itertuples():
        test = math.isnan(float(note.imdb_ratings))
        if test is True:
            movie_ratings = movie_ratings.drop(movie_ratings.index[i])
            i -= 1
        i += 1
    return movie_ratings



def replace_metascore(movie_ratings):
    '''
    We replace the metascore by imdb score if the metascore does not exist
    
    :param dataframe movie_ratings: dataframe with all the data from movies
    :return dataframe movie_ratings: dataframe with all the data from movies
    :rtype: dataframe
    
    '''
    i = 0
    for note in movie_ratings.itertuples():
        test = math.isnan(float(note.metascore))
        if test is True:
            movie_ratings['metascore'] = movie_ratings['metascore'].replace(movie_ratings['metascore'][i], note.imdb_ratings*10)
        i += 1
    return movie_ratings

    


def clean_dataframe_scrapping(movie_ratings,genres1,genres2,genres3,stars1,stars2,stars3):
    '''
    All the procedures that we need to clean the data frame: 
        drop mv_page, imdb_ratings 
        set on index movie
        labelize the category
        delete line without imdb_ratings
        replace metascore
    
    :param1 movie_ratings: dataframe with all the dataframe from movies
    :return dataframe movie_ratings: clean dataframe with all the dataframe from movies 
    :rtype: dataframe
    '''

    #movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
    movie_ratings = movie_ratings.drop(["year"],axis=1)
    #movie_ratings = movie_ratings.drop(["Unnamed: 0"],axis=1)
    movie_ratings = movie_ratings.drop(["rank"],axis=1)
    movie_ratings = movie_ratings.drop(["category"],axis=1)
    movie_ratings = movie_ratings.set_index('movie')    

    movie_ratings = api.API_search_director(movie_ratings)   #Récupération du directeur avec l'API
    movie_ratings['runtime'] = pd.to_numeric(movie_ratings['runtime'])
    movie_ratings['budget'] = pd.to_numeric(movie_ratings['budget']) 
    movie_ratings['gross'] = pd.to_numeric(movie_ratings['gross'])

    # movie_ratings['runtime'] = movie_ratings['runtime'].fillna(movie_ratings['runtime'].mean())
    # movie_ratings['budget'] = movie_ratings['budget'].fillna(movie_ratings['budget'].mean())
    # movie_ratings['gross'] = movie_ratings['gross'].fillna(movie_ratings['gross'].mean())
    
    movie_ratings = replace_metascore(movie_ratings)
    movie_ratings = add_0_win_nom(movie_ratings)
    
    movie_ratings = act.imputation_previous_value(movie_ratings)
    movie_ratings = movie_ratings.dropna()
    movie_ratings = act.labelisation(movie_ratings,genres1,genres2,genres3,stars1,stars2,stars3)
    
    return movie_ratings

def clean_dataframe(movie_ratings,genres1,genres2,genres3,stars1,stars2,stars3):
    '''
    All the procedures that we need to clean the data frame: 
        drop mv_page, imdb_ratings 
        set on index movie
        labelize the category
        delete line without imdb_ratings
        replace metascore
    
    :param1 movie_ratings: dataframe with all the dataframe from movies
    :return dataframe movie_ratings: clean dataframe with all the dataframe from movies 
    :rtype: dataframe
    '''

    movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
    movie_ratings = movie_ratings.drop(["year"],axis=1)
    movie_ratings = movie_ratings.drop(["Unnamed: 0"],axis=1)
    movie_ratings = movie_ratings.drop(["rank"],axis=1)
    movie_ratings = movie_ratings.drop(["category"],axis=1)
    movie_ratings = movie_ratings.set_index('movie')    

    movie_ratings['runtime'] = pd.to_numeric(movie_ratings['runtime'])
    movie_ratings['budget'] = pd.to_numeric(movie_ratings['budget']) 
    movie_ratings['gross'] = pd.to_numeric(movie_ratings['gross'])

    movie_ratings['runtime'] = movie_ratings['runtime'].fillna(movie_ratings['runtime'].mean())
    movie_ratings['budget'] = movie_ratings['budget'].fillna(movie_ratings['budget'].mean())
    movie_ratings['gross'] = movie_ratings['gross'].fillna(movie_ratings['gross'].mean())
    
    movie_ratings = replace_metascore(movie_ratings)
    movie_ratings = add_0_win_nom(movie_ratings)
    
    movie_ratings = act.imputation_previous_value(movie_ratings)
    movie_ratings = movie_ratings.dropna()
    movie_ratings = act.labelisation(movie_ratings,genres1,genres2,genres3,stars1,stars2,stars3)
    
    return movie_ratings


def add_0_win_nom(movie_ratings):
    
    col = ['win','nom']
    for c in col:
        i = 0
        for ind in movie_ratings[c]:
            test = math.isnan(float(ind))
            if test is True:
                movie_ratings[c][i] = 0
            else:
                pass
            i += 1
    
    return movie_ratings

