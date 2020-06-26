# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:21:56 2020

@author: Alex
"""

import math
import pandas as pd
import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder



def imputation_previous_value(movie_ratings):
    '''
    Imputation in genre2, genre3, stars2 and stars3 of the previus value tu avoid Nan value 
    in order to analyse the data.
    
    :param dataframe movie_ratings: dataframe with all the dataframe from movies
    :return dataframe movie_ratings:dataframe with all the dataframe from movies
    :rtype: dataframe
    '''
    
    i = 0 
    for genre in movie_ratings['genres2']:
        string_test = isinstance(genre, str)  
        if genre != genre :
            movie_ratings['genres2'][i] = movie_ratings['genres1'][i]
        else:
            pass
        i += 1
    
    i = 0 
    for genre in movie_ratings['genres3']:
        string_test = isinstance(genre, str)
        if genre != genre :
            movie_ratings['genres3'][i] = movie_ratings['genres2'][i]
        else:
            pass
        i += 1
        
        # Same proccess for stars : We copy the last stars to avoid Nan cells
        
    i = 0 
    for genre in movie_ratings['stars2']:
        string_test = isinstance(genre, str)  
        if genre != genre :
            movie_ratings['stars2'][i] = movie_ratings['stars1'][i]
        else:
            pass
        i += 1
    
    i = 0 
    for genre in movie_ratings['stars3']:
        string_test = isinstance(genre, str)
        if genre != genre :
            movie_ratings['stars3'][i] = movie_ratings['stars2'][i]
        else:
            pass
        i += 1
    print(movie_ratings.info())
    return movie_ratings

    
def labelisation(movie_ratings,genres1,genres2,genres3,stars1,stars2,stars3):
    '''
    Labelisation of genre2, genre3, stars2 and stars3 in order to analyse the data.
    
    :param dataframe movie_ratings: dataframe with all the dataframe from movies
    :return dataframe movie_ratings:dataframe with all the dataframe from movies
    :rtype: dataframe
    '''
    
    df = movie_ratings
    
    print(df.info())
    
    col1 = genres1    #genre 1 
    col2 = genres2    #genre 2
    col3 = genres3   #genre 3 
    col4 = stars1    #stars 1
    col5 = stars2    #stars 2
    col6 = stars3   #stars 3
    
    
    ##########################################################
    ###################  PARTIE GENRES  ######################
    ##########################################################
        
    first_part = [] 
    second_part = []
    third_part = []
    
    y_genre = df.iloc[:,col1]
    y_genre = y_genre.append(df.iloc[:,col2])
    y_genre = y_genre.append(df.iloc[:,col3])

    
    #y_genre = y_genre.reset_index()
    #y_genre = y_genre.drop(["index"],axis=1)
    
    tier = int(len(y_genre)/3)
    tier2 = int((len(y_genre)/3)*2)
    
    encoder = LabelEncoder()
    normal_y = encoder.fit_transform(y_genre)

    
    i = 0
    while i < len(normal_y):
        if i < tier:
            first_part.append(normal_y[i])
            i += 1
        elif i >= tier and i < tier2:
            second_part.append(normal_y[i])
            i += 1
        elif i >= tier2:
            third_part.append(normal_y[i])
            i += 1
    
    
    movie_ratings['genres1'] = first_part
    movie_ratings['genres2'] = second_part
    movie_ratings['genres3'] = third_part
    
    
    ##########################################################
    ###################  PARTIE STARS  #######################
    ########################################################## 
    
    first_part = [] 
    second_part = []
    third_part = []
    
    
    y_stars = df.iloc[:,col4]
    y_stars = y_stars.append(df.iloc[:,col5])
    y_stars = y_stars.append(df.iloc[:,col6])
    
    #y_stars = y_stars.reset_index()
    #y_stars = y_stars.drop(["index"],axis=1)
    
    tier = int(len(y_stars)/3)
    tier2 = int((len(y_stars)/3)*2)
    
    encoder2 = LabelEncoder()
    normal_y2 = encoder2.fit_transform(y_stars)
    
    
    i = 0
    while i < len(normal_y2):
        if i < tier:
            first_part.append(normal_y2[i])
            i += 1
        elif i >= tier and i < tier2:
            second_part.append(normal_y2[i])
            i += 1
        elif i >= tier2:
            third_part.append(normal_y2[i])
            i += 1
    
    movie_ratings['stars1'] = first_part
    movie_ratings['stars2'] = second_part
    movie_ratings['stars3'] = third_part
    
    label_genre = []
    label_genre = encoder.inverse_transform(normal_y)  

    label_star = []
    label_star = encoder2.inverse_transform(normal_y2) 
    
    df = pd.DataFrame({'index': normal_y,'genres':label_genre})
    df.to_csv('correspondances_genres.csv')
    
    df2 = pd.DataFrame({'index': normal_y2,'stars':label_star})
    df2.to_csv('correspondances_stars.csv')
    
    return movie_ratings


def return_genre_label(genre):
    '''
    Return the label of a genre entered in the function launch_prediction 
    
    :param String genre: genre of the movie
    :return sub: label of the genre
    :rtype: int
    '''
    
    df = pd.read_csv('correspondances_genres.csv')
    subset = df['index'] [ df.genres == genre].values
    sub = subset[0]
    
    return sub

def return_star_label(stars):
    '''
    Return the label of a star entered in the function launch_prediction 
    
    :param String genre: star of the movie
    :return sub: label of the star
    :rtype: int
    '''
    
    df = pd.read_csv('correspondances_stars.csv')
    subset = df['index'] [ df.stars == stars].values
    sub = subset[0]
    
    return sub

    