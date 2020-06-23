# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:34:46 2020
@author: Victor HENRIO
"""

import fonction_scraping_film as fctmv

from IPython.core.display import clear_output
from warnings import warn
from time import time

start_time = time()

#def extraction_data(mv_containers,names, years, imdb_ratings, metascores, votes, categories, mv_pages): 
def extraction_data(mv_containers , mv_attributs): 
        
    '''
    Cleaning of the data contained in the container and then upload in their respective list

    :param string mv_container : contains all the informations of a film present in the container
    :param tupe mv_attributs : contains all the informations of a film present in the container
    :return tupe mv_attributs: tupe of all the data frome movies
    :rtype: tupe of list
    '''
    
    category_film = ['R','PG','PG-13']

         
# For every movie of these 50
    for container in mv_containers:
            
        if container.p.find('span', class_='certificate') is not None:
            
            #Scrape the category and verify if it's a movie (movie type and parental guidancee: R, PG, PG13)
            category = container.p.find('span', class_='certificate').text
            if category_film.count(category)>0 :
                mv_attributs[5].append(category)
                
                # Scrape the name
                if container.h3.a is not None:
                    name = container.h3.a.text
                    name = str(name)
                    mv_attributs[0].append(name)

                else:
                    mv_attributs[0].append(None)
                    
        
                # Scrape the year
                    
                if container.h3.find('span', class_ = 'lister-item-year') is not None:
                    year = container.h3.find('span', class_ = 'lister-item-year').text
                    year = year.translate({ord(c): " " for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."})
                    mv_attributs[1].append(year.replace('(','').replace(')','').strip())
                else:
                    mv_attributs[1].append(None) 
                    
                # Scrape the IMDB rating
                if container.strong is not None:
                    imdb = container.strong.text
                    mv_attributs[2].append(imdb)
                else:
                    mv_attributs[2].append(None)
                    
                # Scrape the Metascore
                if container.find('span', class_ = 'metascore') is not None:
                    m_score = container.find('span', class_ = 'metascore').text
                    mv_attributs[3].append(m_score)
                else:
                    mv_attributs[3].append(None)
                    
        
                # Scrape the number of votes
                if container.find('span', attrs = {'name':'nv'}) is not None:
                    vote = container.find('span', attrs = {'name':'nv'})['data-value']
                    mv_attributs[4].append(vote)
                else:
                    mv_attributs[4].append(None)
                    
                
                # Scrap the URL of the movie 
                if container.h3.find('a') is not None:
                    mv_page = container.h3.find('a').get('href')
                    url = "https://imdb.com" + str(mv_page)
                    mv_attributs[6].append(url)
                else:
                    mv_attributs[6].append(None)                
                
                print("URL:",url)
                mv_attributs = fctmv.extraction_movie_data_from_link(url, mv_attributs)
                
                # Delete every "," in the titles 
                i = 0
                for i in range(len(mv_attributs[0])):
                    mv_attributs[0][i] = clean_title(mv_attributs[0][i])
                    i += 1                 

    return mv_attributs



def monitor_request(nb_requests):
    '''
    Monitor of the request time for debugging and control

    :param int requests: number of request which be put in the message
    :return: void
    :rtype: None
    '''
    
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(nb_requests, nb_requests / elapsed_time))
    clear_output(wait=True)


def warning_request(response, nb_requests):
    '''
    Throw a warning for any status codes different than 200

    :param string response:
    :return: void
    :rtype: None
    '''
    
    if response.status_code != 200:
        warn(': {}; Status code: {}'.format(nb_requests, response.status_code))

def years_loop(nb_years):
    '''
    Return the period that we want to get the films

    :param int nb_years:
    :return list period: the period with all years
    :rtype: list of int
    '''
    
    year = 2020
    i = 0
    period = []
    for i in range(nb_years):
        period.append(year)
        year = year - 1

    return period


def nb_page(number):
    '''
    Return the number of page.s to get

    :param int number:
    :return list nb_page: a list of numbers
    :rtype: list of int   
    '''
    i = 0
    page = 0
    nb_page = []
    for i in range(number):
        nb_page.append(page)
        if i == 0:
            page += 51
        else:
            page +=50

    return nb_page

def clean_chars(chain_to_clean):
    '''
    Delete any other chars than numbers
    
    :param string chain_to_clean: The string to clean
    :return string cleaned_chain: The cleaned string 
    :rtype: string
    '''
   
    chain_to_clean = chain_to_clean.translate({ord(c): "" for c in r"#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
    cleaned_chain = chain_to_clean.replace(f"\n","").strip()
    #chain_to_clean = int(chain_to_clean)
    return cleaned_chain
 
def clean_title(title_to_clean):
    '''
    Delete coma from a string
    
    :param string chain_to_clean: The string to clean
    :return string cleaned_title: The cleaned title
    :rtype: string 
    '''

    cleaned_title = title_to_clean.replace(",","")
    return cleaned_title
