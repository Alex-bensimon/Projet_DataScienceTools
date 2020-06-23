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
    genre1 = []         #7
    genre2 = []         #8
    genre3 = []         #9
    stars1 = []         #10
    stars2 = []         #11
    stars3 = []         #12
    rank = []           #13
    nb_oscar = []       #14
    win = []            #15
    nom = []            #16
    runtime = []        #17
    budget = []         #18
    gross = []          #19
        
    mv_attributs =  names,years,imdb_ratings,metascores,votes,categories,mv_pages,genre1,genre2,genre3,stars1,stars2,stars3,rank,nb_oscar,win,nom,runtime,budget,gross
    
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
        'genres1' : mv_attributs[7],
        'genres2' : mv_attributs[8],
        'genres3' : mv_attributs[9],
        'stars1' : mv_attributs[10],
        'stars2' : mv_attributs[11],
        'stars3' : mv_attributs[12],
        'rank' : mv_attributs[13],
        'nb_oscar' : mv_attributs[14],
        'win' : mv_attributs[15],
        'nom' : mv_attributs[16],
        'runtime' : mv_attributs[17],
        'budget' : mv_attributs[18],
        'gross' : mv_attributs[19]

    })
        
    return movie_ratings