
import bs4
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import fonction_scraping as scrap



genres = []

page_link = f'https://www.imdb.com/title/tt7286456/?ref_=hm_fanfav_tt_2_pd_fp1'
response = requests.get(page_link)
html = bs4.BeautifulSoup(response.text, 'html.parser')

#fin the movie title and the released date
title = html.find('div', class_='title_wrapper')
film_titre_date = title.h1.text
print(film_titre_date)

stars = []
for credit in html.find_all('div', class_='credit_summary_item'):
    inline = credit.h4.text
    if inline == "Stars:":
        for a in credit.find_all('a'):
            href = a.get('href')
            if href != "fullcredits/":
                stars.append(a.text)

print(stars)


#find the movie genres
div = html.find('div', class_="subtext")
for balise in div.find_all('a'):
    title = balise.get('title')
    if title is None:
        genres.append(balise.text)

print(genres)

award = html.find('div', id='titleAwardsRanks', class_='article highlighted')
if award is not None:

    #movie rank
    if award.find('strong') is not None:
        strong = award.find('strong')
        rank = strong.text.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
        rank = int(rank)
        print("rank")
        print(rank)
    #oscars, wins and nominations
    if award.find_all('span', class_="awards-blurb") is not None:

        for span in award.find_all('span', class_="awards-blurb"):

            nwspan = span.text.translate({ord(c): "" for c in "./\ "})
            length = len(nwspan)
            print(length)
            first_word = nwspan[:length-11]
            first_word = first_word[2:]
            print(first_word)
            osc_bool = False

            #if there is/are oscar/s
            if span.find('b') is not None:
                nb_oscar = span.find('b').text.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
                nb_oscar = int(nb_oscar)
                print("nb oscar int")
                print(nb_oscar)
                osc_bool = True

            #if there is/are oscar/s
            elif osc_bool == True:
                print("Win & Nomination")
                length = len(span.text)
                win = span.text[:length-24]
                print("win")
                print(win)
                win = int(win.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "}))
                print("win int")
                print(win)
                nom = span.text[32:]
                print("nom")
                print(nom)
                nom = int(nom.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "}))
                print("nom int")
                print(nom)
            #if not
            else:
                length = len(span.text)
                win = span.text[:length-24]
                win = int(win.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "}))
                print("win")
                print(win)
                nom = span.text[15:]
                nom = int(nom.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "}))
                print("nom")
                print(nom)
#print(rank)




for div in html.find_all('div', class_="txt-block"):
    if div.find('h4', class_='inline') is not None:
        inline = div.find('h4', class_='inline').text
        #find the runtime in minutes
        if inline == "Runtime:":
            runtime = div.find('time')
            runtime = runtime.text.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
            runtime = int(runtime)
            print("runtime")
            print(runtime)
        #find the movie budget
        if inline == "Budget:":
            budget = div.text
            budget = budget.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
            budget = int(budget)
            print("Budget")
            print(budget)
        #find the movie worldwide gross
        if inline == "Cumulative Worldwide Gross:":
            gross = div.text
            gross = gross.translate({ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
            gross = int(gross)
            print("Gross")
            print(gross)



