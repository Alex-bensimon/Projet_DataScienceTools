# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:39 2020
@author: Victor HENRIO
"""

import math
import pandas as pd
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
            movie_ratings['metascore'] = movie_ratings['metascore'].replace(movie_ratings['metascore'][i], note.imdb_ratings)
        i += 1
    return movie_ratings




def labelisation_attributs(movie_ratings,row1,row2,row3):
    
    df = movie_ratings
    
    first_part = []
    second_part = []
    third_part = []
    
    y = df.iloc[:,row1]
    y = y.append(df.iloc[:,row2])
    y = y.append(df.iloc[:,row3])
    
    y = y.reset_index()
    y = y.drop(["index"],axis=1)
    
    print(y)
    
    tier = int(len(y)/3)
    tier2 = int((len(y)/3)*2)
    
    
    encoder = LabelEncoder()
    normal_y = encoder.fit_transform(y)
    # encoder = LabelBinarizer()
    # test = encoder.fit_transform(y)
    
    i = 0
    while i < len(normal_y):
        if i <= tier:
            first_part.append(normal_y[i])
            i += 1
        elif i >= tier and i < tier2:
            second_part.append(normal_y[i])
            i += 1
        elif i >= tier2:
            third_part.append(normal_y[i])
            i += 1
            
    print(row1)
    
    
    movie_ratings[row1] = first_part
    movie_ratings[row2] = second_part
    movie_ratings[row3] = third_part
    
    print("---"*30)
    print(movie_ratings)
    print("---"*30)
    return movie_ratings
    


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
    
    # Replace the object type by int or float
    movie_ratings['movie'] = movie_ratings['movie'].replace(",","")
    #movie_ratings['year'] = movie_ratings['year'].apply(pd.to_numeric) 
    movie_ratings['imdb_ratings'] = movie_ratings['imdb_ratings'].astype(float)
    movie_ratings['metascore'] = movie_ratings['metascore'].astype(float)
    movie_ratings['imdb_ratings'] = movie_ratings['imdb_ratings'].astype(float)
    movie_ratings['votes'] = movie_ratings['votes'].astype(int)
    movie_ratings['runtime'] = movie_ratings['runtime'].apply(pd.to_numeric)
    movie_ratings['nb_oscar'] = movie_ratings['nb_oscar'].astype(int)
    movie_ratings['win'] = movie_ratings['win'].apply(pd.to_numeric)
    movie_ratings['nom'] = movie_ratings['nom'].apply(pd.to_numeric)
    movie_ratings['budget'] = movie_ratings['budget'].apply(pd.to_numeric)
    movie_ratings['gross'] = movie_ratings['gross'].apply(pd.to_numeric)
    
    movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
    movie_ratings = movie_ratings.drop(["rank"],axis=1)
    #movie_ratings = movie_ratings.set_index('movie')
    movie_ratings['category'] = movie_ratings['category'].replace(regex={'R': '1','PG-13': '3', 'PG': '2'})
    movie_ratings = delete_raws_nan(movie_ratings)
    movie_ratings['runtime']=movie_ratings['runtime'].fillna(movie_ratings['runtime'].mean())
    movie_ratings = replace_metascore(movie_ratings)

    return movie_ratings

#%%

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

