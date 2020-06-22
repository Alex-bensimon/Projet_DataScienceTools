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

print(response.text)
print("---"*30)
binary = response.content
output = json.loads(binary)

#pprint.pprint(output)

film = output['movie_results']
id_film = str(film[0]['id'])

credits_url = "https://api.themoviedb.org/3/movie/"+id_film+"/credits?api_key=9c78e72fe9af9417e5682302b1ed0f8a"
film_credits = requests.get(credits_url)
bina = film_credits.content
output2 = json.loads(bina)

#print(film_credits.text)


cred = output2['cast']['department']
print(cred)
i=0
for cred in id_:
    cred = str(id_[i]['department'])
    i += 1

#test = cred['Directing']

    




