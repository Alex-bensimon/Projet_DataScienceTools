# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:09:35 2020
@author: Alex
"""
#def add_director(movie_ratings):

import requests,json,pprint
import pandas as pd

movie_ratings = pd.read_csv('movie_ratings_1980_2000_p10.csv')

link = movie_ratings['mv_page'][1][23:][:-1]
print(link)

url = "https://api.themoviedb.org/3/find/"+link+"?api_key=9c78e72fe9af9417e5682302b1ed0f8a&language=en-US&external_source=imdb_id"
print(url)
response = requests.get(url)

#print(response.text)

binary = response.content
output = json.loads(binary)

pprint.pprint(output)

print("---"*30)

film = output['movie_results']
id_film = str(film[0]['id'])

credits_url = "https://api.themoviedb.org/3/movie/"+id_film+"/credits?api_key=9c78e72fe9af9417e5682302b1ed0f8a"
film_credits = requests.get(credits_url)
bina = film_credits.content
output2 = json.loads(bina)

print(film_credits.text)

print("---"*30)

# cred = output2['crew'][1]['job']
# print(cred)

i=0
test= False
while test != True :
    job = output2['crew'][i]['job']
    if job == 'Director':
        test = True
        director = output2['crew'][i]['name']
        print(director)
    else :
        test = False
        i+=1
        
link = movie_ratings['mv_page'][1][23:][:-1]
filter = movie_ratings["mv_page"][1][23:][:-11] == link

#movie_ratings['director'] = director.where(filter, inplace = True) 
movie_ratings['director'].where(filter, inplace = True) = director 

    #return movie_ratings