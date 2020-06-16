# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:45:39 2020

@author: Victor HENRIO
"""
import pandas as pd

def data_frame_netoyage(names,years,imdb_ratings,metascores,votes,categories):
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
        'categories':categories
    })
    
    print(movie_ratings.info())
    
    movie_ratings.head(10)
    
    movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
    
    movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
    
    movie_ratings.to_csv('movie_ratings2.csv')
    
    print(movie_ratings.head(10))
    
    return movie_ratings


#def plot_graph():

        # fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
        # ax1, ax2, ax3 = fig.axes
        # ax1.hist(movie_ratings['imdb'], bins = 10, range = (0,10)) # bin range = 1
        # ax1.set_title('IMDB rating')
        # ax2.hist(movie_ratings['metascore'], bins = 10, range = (0,100)) # bin range = 10
        # ax2.set_title('Metascore')
        # ax3.hist(movie_ratings['n_imdb'], bins = 10, range = (0,100), histtype = 'step')
        # ax3.hist(movie_ratings['metascore'], bins = 10, range = (0,100), histtype = 'step')
        # ax3.legend(loc = 'upper left')
        # ax3.set_title('The Two Normalized Distributions')
        # for ax in fig.axes:
        #     ax.spines['top'].set_visible(False)
        #     ax.spines['right'].set_visible(False)   
        # plt.show()