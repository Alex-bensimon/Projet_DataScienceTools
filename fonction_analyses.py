# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:39 2020
@author: Victor HENRIO
"""

import math
import pandas as pd

def delete_raws_nan(movie_ratings):
    '''
    If there is not a specific attribut we delete the ligne cause
    
    :param1 dataframe movie_ratings: with all the dataframe from movies,
    :return dataframe movie_ratings: with all the dataframe from movies
    :rtype: dataframe
    
    '''

    i = 0
    for note in movie_ratings.itertuples():
        test = math.isnan(float(note.n_ratings))
        if test is True:
            movie_ratings = movie_ratings.drop(movie_ratings.index[i])
            i -= 1
        i += 1
    return movie_ratings





def replace_metascore(movie_ratings):
    '''
    We replace the metascore by imdb score if the metascore does not exist
    
    :param dataframe movie_ratings: dataframe with all the dataframe from movies
    :return dataframe movie_ratings:dataframe with all the dataframe from movies
    :rtype: dataframe
    
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



def replace_nan(movie_ratings):
    '''
    
    '''
    


"""
def actors_to_num(movie_ratings):
    '''
    '''

    df = movie_ratings
    acteurs = []
    acteurs = df['stars']
    list_acteur = []
    index_acteurs = []

    index = 0
    for act in acteurs:
        if act in list_acteur:
            index_acteurs.append(list_acteur.index(act))
        else: 
            list_acteur.append(act)
            index_acteurs.append(index)
            index += 1

    #table_corres_df = np.array([index_acteurs, temp])
    len_list_acteur = []
    i = 0
    for i in range(len(list_acteur)):
        len_list_acteur.append(i)
    #print(len_list_acteur)
    df2 = pd.DataFrame({'Index': len_list_acteur,'Acteur': list_acteur})
    df2 = df2.set_index('Index')
    #print(df2)
    df2.to_csv('table_correspondance_acteurs.csv')

    
    return index_acteurs
"""


def clean_dataframe(movie_ratings):
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
    movie_ratings = movie_ratings.drop(["imdb_ratings"],axis=1)
    movie_ratings = movie_ratings.set_index('movie')
    movie_ratings['category'] = movie_ratings['category'].replace(regex={'R': '1','PG-13': '3', 'PG': '2'})
    movie_ratings = delete_raws_nan(movie_ratings)
    movie_ratings = replace_metascore(movie_ratings)

    return movie_ratings