# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:30:48 2020

@author: Victor HENRIO
"""


import fonction_scraping_accueil as scrap
import fonction_traitement as trait
import definition_tab as dftab

from bs4 import BeautifulSoup
from requests import get



def scraping_total(nb_years,nb_pages):

    
    mv_attributs = dftab.instanciation_tablist()
      
    # Parameters
    
    years_url = scrap.years_loop(nb_years)
    pages = scrap.nb_page(nb_pages)
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    
    #SCRAPPING :
    
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
        
    movie_ratings = dftab.creation_dataframe(mv_attributs)
    
    print(movie_ratings.info())
    movie_ratings = trait.clean_dataframe_scrapping(movie_ratings,4,5,6,7,8,9) 
    
    movie_ratings.to_csv("./Data_csv/Nouveau_scraping.csv")

    return movie_ratings

