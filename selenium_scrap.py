# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:49:34 2020
@author: Alex
"""

import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests


page_link = f'http://www.allocine.fr/film/meilleurs/boxoffice/'
response = requests.get(page_link)
html = bs4.BeautifulSoup(response.text, 'html.parser')

tab = []
liens = []
tab = html.find_all('a', attrs={'class': 'meta-title-link'})
for titre in tab:
    liens.append(titre.get('href'))
print(liens)