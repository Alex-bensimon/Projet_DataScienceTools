# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:49:34 2020
@author: Jules
"""

import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests


#wd = webdriver.Chrome(r"C:\Users\Alex\Documents\chromedriver_win32\chromedriver")

#driver = wd.get(f"http://www.allocine.fr/film/meilleurs/boxoffice/")
#sleep(3)
#response = requests.get(driver)
#print(response)
#html = BeautifulSoup(response.text, 'html.parser')

page_link = f'http://www.allocine.fr/film/meilleurs/boxoffice/'
response = requests.get(page_link)
html = bs4.BeautifulSoup(response.text, 'html.parser')

tab = []
liens = []
tab = html.find_all('a', attrs={'class': 'meta-title-link'})
for titre in tab:
    liens.append(titre.get('href'))
print(liens)
#link = driver.find_element_by_link_text("Titanic")
#link.click()


#wd.close()