
import bs4
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)

genres = []

page_link = f'https://www.imdb.com/title/tt7286456/?ref_=hm_fanfav_tt_2_pd_fp1'
response = requests.get(page_link)
html = bs4.BeautifulSoup(response.text, 'html.parser')

#fin the movie title and the released date
title = html.find('div', class_='title_wrapper')
film_titre_date = title.h1.text
print(film_titre_date)


#find the movie genres
sub = html.find('div', class_="subtext")
for balise in sub.find_all('a'):
    href = balise.get('href')
    if href != "/title/tt7286456/releaseinfo":
        genres.append(balise.text)
print(genres)

award = html.find('div', id='titleAwardsRanks', class_='article highlighted')
if award is not None:
    print("1")
    if award.find('a', href="/chart/top?ref_=tt_awd") is not None:
        print("2")
        rank = html.find('a', href="/chart/top?ref_=tt_awd").text[18:]
    if award.find_all('span', class_="awards-blurb") is not None:
        print("3")
        nb_span = 1
        for span in award.find_all('span', class_="awards-blurb"):
            if nb_span == 1:
                nb_oscar = span.text.translate({ord(c): " " for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."})
                nb_oscar = int(nb_oscar)
                nb_span+=1
            else:
                print("5")
                win_nom = span.text.translate(
                    {ord(c): " " for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&."})
                for i in range(0,len(win_nom)-1):

                    nb_span += 1


#print(rank)
print(nb_oscar)
print(win_nom)
"""
for div in html.find_all('div', class_="txt-block"):
    if div.find('h4', class_='inline') is not None:
        inline = div.find('h4', class_='inline').text
        #find the runtime in minutes
        if inline == "Runtime:":
            runtime = div.text[9:]
            runtime = int(runtime[:-5])
        #find the movie budget
        if inline == "Budget:":
            budget = div.text[9:]
            if div.find('span', class_="attribute") is not None:
                budget = budget[:11]
            budget = int(budget.replace(',', ''))
        #find the movie worldwide gross
        if inline == "Cumulative Worldwide Gross:":
            gross = div.text[30:]
            if div.find('span', class_="attribute") is not None:
                gross = gross[:10]
            gross = int(gross.replace(',',''))
print(runtime)
print(budget)
print(gross)
replace('\n','').replace('a','').replace('A','').replace('b','').\
                    replace('B','').replace('c','').replace('C','').replace('d','').\
                    replace('D','').replace('e','').replace('E','').replace('f','').\
                    replace('F','').replace('g','').replace('G','').replace('h','').\
                    replace('H','').replace('i','').replace('I','').replace('j','').\
                    replace('J','').replace('k','').replace('K','').replace('l','').\
                    replace('L','').replace('m','').replace('M','').replace('n','').\
                    replace('N','').replace('o','').replace('O','').replace('N','').\
                    replace('o','').replace('O','').replace('(','').\
                    replace(')','').replace('.','')
"""