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

# Tabs 
names = []
years = []
imdb_ratings = []
metascores = []
votes = [] 
categories = []
mv_pages = []
    
    
# Preparing the monitoring of the loop
start_time = time()
nb_requests = 0
years_url = scrap.years_loop(3)
pages = scrap.nb_page(3)
headers = {"Accept-Language": "en-US, en;q=0.5"}

#SCRAPPING :

# A request would go here
#nb_requests += 1
#sleep(randint(1,3))
#scrap.monitor_request(nb_requests)

# For every year in the interval 2000-2002
for year_url in years_url:

    # For every page in the interval 1-3
    for page in pages:

        # Make a get request
        response = get('http://www.imdb.com/search/title?release_date=' + str(year_url) +
        '&sort=num_votes,desc&page=' + str(page), headers = headers)

        # Pause the loop
        # sleep(randint(8,15))
        
        #nb_requests += 1
        
        # Monitor the requests :    
        #scrap.monitor_request(nb_requests)

        # Throw a warning for non-200 status codes
        #scrap.warning_request(response, nb_requests)

        # Break the loop if the number of requests is greater than expected
        #if nb_requests > 2:
            #   warn('Number of requests was greater than expected.')
            #  break

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        #Take the information from the containers
        names, years, imdb_ratings, metascores, votes, categories, mv_pages = scrap.extraction_data(mv_containers,names, years, imdb_ratings, metascores, votes, categories, mv_pages)
        

        # Create Data Frame :
        
movie_ratings = analy.data_frame_netoyage(names,years,imdb_ratings,metascores,votes,categories,mv_pages)

  

#%%

#Partie Analyse 

import numpy as np 
import pandas as pd

movie_ratings.to_csv('movie_ratings3.csv')

movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
movie_ratings = movie_ratings.drop(["category"],axis=1)
movie_ratings = movie_ratings.set_index('movie')

print(movie_ratings.info())
print(movie_ratings.describe())

#scikit-learn
import sklearn
#classe pour standardisation
from sklearn.preprocessing import StandardScaler
#instanciation
sc = StandardScaler()
#transformation – centrage-réduction
Z = sc.fit_transform(movie_ratings)
print(Z)




