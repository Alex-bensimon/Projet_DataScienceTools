"""
Created on Sun Jun 14 14:43:49 2020
@author: Alex
"""
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import urllib.request
import pandas as pd

#first commentaire

page_link = f'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(page_link)
html = BeautifulSoup(response.text, 'html.parser')

rows = []
rows.append(['Null', 'Lien','Note', 'Note2','Null2'])
print(rows)

table = html.find('table', attrs={'class': 'chart full-width'})
results = table.find_all('tr')
print('Number of results', len(results))

titre = []
date = []
note = []
# loop over results
for result in results:
# find all columns per result
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    else:
        titre.append(data[1].text.replace('\n','').replace(str(0),'').
                         replace(str(1),'').replace(str(2),'').
                         replace(str(3),'').replace(str(4),'').
                         replace(str(5),'').replace(str(6),'').
                         replace(str(7),'').replace(str(8),'').
                         replace(str(9),'').replace('(','').
                         replace(')','').replace('.','').replace('            ',''))
        date.append(int(data[1].text.replace('\n','').replace('(','').
                   replace(')','')[-4:]))
        note.append(float(data[2].text.replace('\n','')))

#print('Titre : ', titre)
#print('Date : ', date)
#print('Note : ', note)

df2 = pd.DataFrame({'Titre ':titre,'Date de sortie':date,
                        'Note ':note,})
print(df2)
print(df2.describe())


'''
    Extract book links from URL_BOOK_LISTE
    :param root_html: BeautifulSoup Element that contains all books links
    :type book_html: bs4.BeautifulSoup
    :return: List of all book links in the page
    :rtype: list(str)
# TODO Append to books_links all the links refering to Books you may find on this page.
films_links = []
# First find all links
for element in html.find_all('a'):
    #ref = element['href']
    ref = html.find('a').get('href')
    if "/title/" in ref:
        films_links.append(ref)
url = html.find('a').get('href')
page = urllib.request.urlopen(url)
print(url)
'''