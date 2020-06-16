# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:11:18 2020

@author: Victor HENRIO
"""

import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd

page_link = f'https://www.imdb.com/search/title/?release_date=2000'
response = requests.get(page_link)
html = bs4.BeautifulSoup(response.text, 'html.parser')


tab = [] 
liens = []
liens_propre = []


balise_a = html.find_all('a')

for titre in balise_a:
    liens.append(titre.get('href'))
    for l in liens:
        if str(l).startswith('/title/'):
            liens_propre.append(l)

df = pd.DataFrame({'Liens ':liens_propre})
df.drop_duplicates(keep=False)
print(df.describe())