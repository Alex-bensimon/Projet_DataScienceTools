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
years_url = scrap.years_loop(5)
pages = scrap.nb_page(5)
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
        names, years, imdb_ratings, metascores, votes, categories, mv_pages = scrap.extraction_data(mv_containers,names, years, imdb_ratings, metascores, votes, categories, mv_pages)
        

# Create Data Frame : 
movie_ratings = analy.data_frame_netoyage(names,years,imdb_ratings,metascores,votes,categories,mv_pages)

  

#%%

#Partie Analyse 

import numpy as np 
import pandas as pd

movie_ratings.to_csv('movie_ratings3.csv')

movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
movie_ratings = movie_ratings.drop(["imdb_ratings"],axis=1)
movie_ratings = movie_ratings.drop(["category"],axis=1)
movie_ratings = movie_ratings.set_index('movie')

print(movie_ratings.info())
print(movie_ratings.describe())
print(movie_ratings.head(10))


"""
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.feature_selection import RFECV
from sklearn.linear_model import SGDClassifier

X = movie_ratings.drop(["n_imdb"],axis=1).values
y = movie_ratings['n_imdb'].values

print(X.shape)
print(y.shape)

chi2(X, y)
print(chi2(X,y))

<<<<<<< HEAD
selector = SelectKBest(f_classif, k=2)
selector.fit_transform(X, y)

print(selector.get_support())

selector = RFECV(SGDClassifier(random_state=0), step=1, min_features_to_select=2, cv=5)
selector.fit(X, y)
print(selector.ranking_)
print(selector.grid_scores_)
"""
