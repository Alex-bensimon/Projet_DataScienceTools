# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 08:19:10 2020
@author: Victor HENRIO
"""
# %%

import fonction_scraping_accueil as scrap
import fonction_traitement as trait
import definition_tab as dftab
import API as api


#%%

import numpy as np
from bs4 import BeautifulSoup
import time
from requests import get
from time import sleep
from random import randint
from warnings import warn
from time import time
import matplotlib.pyplot as plt
import requests
import pandas as pd


mv_attributs = dftab.instanciation_tablist()
    
  
# Preparing the monitoring of the loop
start_time = time()
nb_requests = 0
years_url = scrap.years_loop(1)
pages = scrap.nb_page(1)
headers = {"Accept-Language": "en-US, en;q=0.5"}

#SCRAPPING :

# A request would go here
#nb_requests += 1
#sleep(randint(1,3))
#scrap.monitor_request(nb_requests)

# For every year in an interval
for year_url in years_url:

    # For every page in an interval 
    for page in pages:

        # Make a get request
        url = 'https://www.imdb.com/search/title/?release_date='+ str(year_url) +'-01-01,'+ str(year_url) +'-12-31&sort=num_votes,desc&start='+ str(page)+'&ref_=adv_nxt'      
        print(url)
        response = get(url, headers = headers)

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        #Take the information from the containers
        mv_attributs = scrap.extraction_data(mv_containers, mv_attributs)
    
print(mv_attributs)

#%%
movie_ratings = dftab.creation_dataframe(mv_attributs)
print(movie_ratings)

#%%

movie_ratings.to_csv('movie_ratings_1980_2000_p10.csv')

#%%
movie_ratings.to_excel ('movie_ratings_1980_2000_p10.xlsx', index = None, header=True)

#%%

#Partie Traitement 

"""
Call the function which changes the type, cleans the dataframe by deleting rows if rating is NaN
and get a metascore based on the imdb rating.
"""
movie_ratings = trait.clean_dataframe(movie_ratings) 

#%%
print(movie_ratings.info())
print(movie_ratings.describe())
print(movie_ratings.head(20))
