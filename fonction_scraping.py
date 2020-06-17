# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:34:46 2020
@author: Victor HENRIO
"""

from IPython.core.display import clear_output
from warnings import warn
from time import time

start_time = time()

<<<<<<< HEAD

def extraction_data(mv_containers):
=======
def extraction_data(mv_containers,names, years, imdb_ratings, metascores, votes, categories, mv_pages): 
        
>>>>>>> master
    '''
    Cleaning of the data contained in the container and then upload in their respective list

    :param mv_container string: contains all the informations of a film present in the container
    :return list names: list of the name film
    :return list years: list of the year film
    :return list imdb_ratings: list of score given by imdb for the movie
    :return list metascores: liste of metascores of the given film
    :return list votes : list of number of votes by movie
    :rtype: listes

    '''
    
    category_film = ['R','PG','PG-13']

         
# For every movie of these 50
    for container in mv_containers:
            
        if container.p.find('span', class_='certificate') is not None:
            #Scrape the category and verify if it's a movie (movie type and parental guidancee: R, PG, PG13)
            category = container.p.find('span', class_='certificate').text
            if category_film.count(category)>0 :
                categories.append(category)
                
                # Scrape the name
                if container.h3.a is not None:
                    name = container.h3.a.text
                    names.append(name)
                else:
                    names.append(None)
                    
        
                # Scrape the year
                    
                if container.h3.find('span', class_ = 'lister-item-year') is not None:
                    year = container.h3.find('span', class_ = 'lister-item-year').text
                    year = year.translate({ord(c): " " for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."})
                    years.append(year.replace('(','').replace(')','').strip())
                else:
                    years.append(None) 
        
                # Scrape the IMDB rating
                if container.strong is not None:
                    imdb = float(container.strong.text)
                    imdb_ratings.append(imdb)
                else:
                    imdb_ratings.append(None)
        
                # Scrape the Metascore
                if container.find('span', class_ = 'metascore') is not None:
                    m_score = container.find('span', class_ = 'metascore').text
                    metascores.append(int(m_score))
                else:
                    metascores.append(None)
                    
        
                # Scrape the number of votes
                if container.find('span', attrs = {'name':'nv'}) is not None:
                    vote = container.find('span', attrs = {'name':'nv'})['data-value']
                    votes.append(int(vote))
                else:
                    votes.append(None)
                    
                
                # Scrap the URL of the movie 
                if container.h3.find('a') is not None:
                    mv_page = container.h3.find('a').get('href')
                    url = "https://imdb.com" + str(mv_page)
                    mv_pages.append(url)
                else:
                    mv_pages.append(None)
                         
    return names, years, imdb_ratings, metascores, votes, categories, mv_pages



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
    """
    Return the period that we want to get the films

    :param int nb_years:
    :return list period: the period with all years
    :rtype: list of int
    """
    year = 2020
    i = 0
    period = []
    for i in range(nb_years):
        period.append(year)
        year = year - 1

    return period


def nb_page(number):
    """
    Return the number of page.s to get

    :param int number:
    :return list nb_page: a list of numbers
    :rtype: list of int
    """
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

