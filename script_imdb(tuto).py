# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 08:19:10 2020

@author: Victor HENRIO
"""
#%%

import fonction_scraping as scrap
import fonction_analyses as analy

import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from requests import get
from time import sleep
from random import randint
from warnings import warn
from time import time
import matplotlib.pyplot as plt

#%%
    
    
# Preparing the monitoring of the loop
start_time = time()
nb_requests = 0
years_url = [2000]
pages = [1]
headers = {"Accept-Language": "en-US, en;q=0.5"}

#SCRAPPING :

for _ in range(5):
# A request would go here
    nb_requests += 1
    sleep(randint(1,3))
    scrap.monitor_request(nb_requests)

    # For every year in the interval 2000-2002
    for year_url in years_url:
    
        # For every page in the interval 1-3
        for page in pages:
    
            # Make a get request
            response = get('http://www.imdb.com/search/title?release_date=' + str(year_url) +
            '&sort=num_votes,desc&page=' + str(page), headers = headers)
    
            # Pause the loop
            # sleep(randint(8,15))
            
            nb_requests += 1
           
            # Monitor the requests :    
            scrap.monitor_request(nb_requests)
    
            # Throw a warning for non-200 status codes
            scrap.warning_request(response, nb_requests)
    
            # Break the loop if the number of requests is greater than expected
            if nb_requests > 2:
                warn('Number of requests was greater than expected.')
                break
    
            # Parse the content of the request with BeautifulSoup
            page_html = BeautifulSoup(response.text, 'html.parser')
    
            # Select all the 50 movie containers from a single page
            mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
    
            #Take the information from the containers
            names, years, imdb_ratings, metascores, votes, categories = scrap.extraction_data(mv_containers)
            
                

        # Create Data Frame :
        
movie_ratings = analy.data_frame_netoyage(names,years,imdb_ratings,metascores,votes,categories)

  
        
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




