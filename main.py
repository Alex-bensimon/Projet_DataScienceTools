# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 08:19:10 2020
@author: Victor HENRIO
"""
# %%

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
import requests

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
        url = 'https://www.imdb.com/search/title/?release_date='+ str(year_url) +'-01-01,'+ str(year_url) +'-12-31&start='+ str(page)+'&ref_=adv_nxt'      
        print(url)
        response = get(url, headers = headers)

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        #Take the information from the containers
        mv_attributs = scrap.extraction_data(mv_containers, mv_attributs)
        
        

# Create Data Frame : 
movie_ratings = analy.data_frame_netoyage(mv_attributs)

  

#%%

#Partie Analyse 

"""
Call the function which cleans the dataframe by deleting rows if rating is NaN
and get a metascore based on the imdb rating.
"""
movie_ratings = analy.clean_dataframe(movie_ratings)

print(movie_ratings.info())
print(movie_ratings.describe())
print(movie_ratings.head(10))

movie_ratings.to_csv('movie_ratings.csv')
