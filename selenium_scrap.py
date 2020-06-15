# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:49:34 2020

@author: Alex
"""


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

wd = webdriver.Chrome(r"C:\Users\Alex\Documents\chromedriver_win32\chromedriver")

driver = wd.get(f"https://www.imdb.com/chart/top/?ref_=nv_mv_250")
sleep(3)

page_link = f'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(page_link)
#html = BeautifulSoup(response.text, 'html.parser')
html = BeautifulSoup(response.text, 'lxml')

rows = [] 
rows.append(['Null', 'Lien','Note', 'Note2','Null2'])

table = html.find('table', attrs={'class': 'chart full-width'})
results = table.find_all('tr')

link = driver.find_element_by_link_text("Le parrain")
link.click()


lien_propre = []
for result in results:
# find all columns per result
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    else:
        lien_propre.append(data[1].find('a').get('href'))
        link = driver.find_element_by_link(lien_propre)
        link.click()

wd.close()