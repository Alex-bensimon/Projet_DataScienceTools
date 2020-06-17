# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 18:34:46 2020

@author: Victor HENRIO
"""

from IPython.core.display import clear_output
from warnings import warn
from time import time
start_time = time()

def extraction_data(mv_containers): 
        
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
####################################################
####################################################

#VERSION IMDB A CHANGER POUR ALLOCINE 

####################################################
####################################################    
      
    titre = []
    nb_entrees = []
    date_sortie = []
    genre = []
    duree = []
    note_spect = []
    note_presse = []
    realisateur = []
    acteurs_principaux = []
    classement = []
    n = []
         
# For every movie of these 50
    for container in mv_containers:
        # If the movie has a Metascore, then:
        if container.find('div', class_ = 'ratings-metascore') is not None:
            
            #Scrape the category and verify if it's a movie
            category = container.p.find('span', class_='certificate').text
            if category == 'R':
                categories.append(category)
                
                # Scrape the name
                name = container.h3.a.text
                names.append(name)
        
                # Scrape the year
                year = container.h3.find('span', class_ = 'lister-item-year').text
                years.append(year)
        
                # Scrape the IMDB rating
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)
        
                # Scrape the Metascore
                m_score = container.find('span', class_ = 'metascore').text
                metascores.append(int(m_score))
        
                # Scrape the number of votes
                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))
                
            else :
                pass
            
            # category = container.p.find('span', class_='certificate').text
            # categories.append(category)
            

        


    return names, years, imdb_ratings, metascores, votes, categories


def monitor_request(nb_requests):
    '''
    Monitor of the request time for debugging and control
    
    :param int requests: number of request which be put in the message
    :return: void
    :rtype: None
    '''    
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(nb_requests, nb_requests/elapsed_time))
    clear_output(wait = True)


def warning_request(response,nb_requests):
    '''
    Throw a warning for any status codes different than 200
    
    :param string response:
    :return: void
    :rtype: None
    
    '''
    if response.status_code != 200:
        warn(': {}; Status code: {}'.format(nb_requests, response.status_code))

  
