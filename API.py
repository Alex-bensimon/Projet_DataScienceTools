# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:09:35 2020
@author: Victor Le KING DU CODE
"""


import requests,json,pprint
import pandas as pd


movie_ratings = pd.read_csv('movie_ratings_10val(test).csv')


#%%

def API_search_director(movie_ratings):
    '''
    Get the name of the director from the API "themoviedb.org" and create a new 
    
    :param dataframe movie_ratings: dataframe with all the dataframe from movies
    :return dataframe movie_ratings:dataframe with all the dataframe from movies
    :rtype: dataframe

    '''

    
    list_director = []
    
    for row in movie_ratings.itertuples():
        
        
        mv_pages = row[7]         
        print(mv_pages)
        link = mv_pages[23:][:-1]
        print("title :", link)
        
        
        url = "https://api.themoviedb.org/3/find/"+link+"?api_key=9c78e72fe9af9417e5682302b1ed0f8a&language=en-US&external_source=imdb_id"
        #print("URL :", url)
        response = requests.get(url)
        
        
        binary = response.content
        output = json.loads(binary)
        
        
        film = output['movie_results']
        id_film = str(film[0]['id'])
        
        credits_url = "https://api.themoviedb.org/3/movie/"+id_film+"/credits?api_key=9c78e72fe9af9417e5682302b1ed0f8a"
        film_credits = requests.get(credits_url)
        bina = film_credits.content
        output2 = json.loads(bina)
        
        
        i=0
        test= False
        existing = False 
        while test != True :
            job = output2['crew'][i]['job']
            if job == 'Director':
                test = True
                director = output2['crew'][i]['name']
                #print("director :", director)
                existing = True
            else :
                test = False
                i+=1
        
        if not existing :
            director = None
        
        list_director.append(director)
        
        
    movie_ratings["director"] = list_director
        
    print (len(list_director))
            
    return movie_ratings
