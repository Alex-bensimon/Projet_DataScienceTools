import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd

page_link = f'https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=WT74SPAM9Y3E34HC68RX&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_ql_3'
response = requests.get(page_link)
html = bs4.BeautifulSoup(response.text, 'html.parser')

tab = []
liens = []
liens_propre = []
tab = html.find_all('a')
for titre in tab:
    liens.append(titre.get('href'))
    for l in liens:
        if str(l).startswith('/title/'):
            liens_propre.append(l)

df = pd.DataFrame({'Liens ':liens_propre})
df.drop_duplicates(keep=False)
print(df.describe())