# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:24:27 2020

@author: Victor HENRIO
"""

import pandas as pd

def instanciation_tablist():
    
        # Tabs 
    names = []          #0
    years = []          #1
    imdb_ratings = []   #2
    metascores = []     #3
    votes = []          #4
    categories = []     #5
    mv_pages = []       #6
    genres = []         #7
    stars = []          #8
    rank = []           #9
    nb_oscar = []       #10
    win = []            #11
    nom = []            #12
    runtime = []        #13
    budget = []         #14
    gross = []          #15
        
    mv_attributs =  names,years,imdb_ratings,metascores,votes,categories,mv_pages,genres,stars,rank,nb_oscar,win,nom,runtime,budget,gross
    
    return mv_attributs



def creation_dataframe(mv_attributs):
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
    movie_ratings['n_ratings'] = movie_ratings['imdb_ratings'] * 10   
    
    return movie_ratings