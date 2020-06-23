# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:09:35 2020
@author: Alex
"""
import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"page":"1","r":"json","s":"Avengers Endgame"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "2a8e04209dmsh59f2ba09f4a5418p1b24fejsn80a905121efb"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

#%%

import requests,json,pprint
url = "https://api.themoviedb.org/3/find/tt0137523?api_key=9c78e72fe9af9417e5682302b1ed0f8a&language=en-US&external_source=imdb_id"

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
        print(output2['crew'][i]['name'])
    else :
        test = False
        i+=1
