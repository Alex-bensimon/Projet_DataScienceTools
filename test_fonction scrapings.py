# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:02:48 2020

@author: Victor HENRIO
"""

from warnings import warn
import bs4
import requests
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import fonction_scraping as scrap


'''
Get some information from a movie link

:param1 String link: http url that point to the movie
:param2 tupe mv_attributs : tupe of all the data frome movies
:return tupe mv_attributs: tupe of all the data frome movies
:rtype: tupe of list

'''
names = []          #0
years = []          #1
imdb_ratings = []   #2
metascores = []     #3
votes = []          #4
categories = []     #5
mv_pages = []       #6
genre1 = []         #7
genre2 = []         #8
genre3 = []         #9
stars1 = []         #10
stars2 = []         #11
stars3 = []         #12
rank = []           #13
nb_oscar = []       #14
win = []            #15
nom = []            #16
runtime = []        #17
budget = []         #18
gross = []          #19
    
mv_attributs =  names,years,imdb_ratings,metascores,votes,categories,mv_pages,genre1,genre2,genre3,stars1,stars2,stars3,rank,nb_oscar,win,nom,runtime,budget,gross


# TEST POSSIBILITIES :

page_link = "https://www.imdb.com/title/tt7286456/" #oscar win nom
#page_link = "https://www.imdb.com/title/tt0120903/" #win nom
#page_link = "https://www.imdb.com/title/tt6914122/" #nom
#page_link = "https://www.imdb.com/title/tt8201852/" #Empty
#page_link ="https://www.imdb.com/title/tt2017038/"  #1 Star


response = requests.get(page_link)
html = bs4.BeautifulSoup(response.text, 'html.parser')

nb_genre = 0
#get the movie genres
div = html.find('div', class_="subtext")
#test_genre = False
for a in div.find_all('a'):
    #test_genre = False
    title = a.get('title')
    #there is a balise title which we do not want
    if title is None:
        mv_attributs[7+nb_genre].append(a.text)
        #test_genre = True
        nb_genre += 1
if nb_genre == 1:
    mv_attributs[8].append(None)
    mv_attributs[9].append(None)
    nb_genre = 3
if nb_genre == 2:
    mv_attributs[9].append(None)
    nb_genre = 3

#get the stars acting in the movie
stars = []
nb_act = 0
#test_stars = False
for credit in html.find_all('div', class_='credit_summary_item'):
    #test_stars = False
    inline = credit.h4.text
    if inline == "Stars:" or "Star":
        for a in credit.find_all('a'):
            href = a.get('href')
            if href != "fullcredits/":
                mv_attributs[10+nb_act].append(a.text)
                #test_stars = True
                nb_act += 1
if nb_act == 0:
    mv_attributs[10].append(None)
    mv_attributs[11].append(None)
    mv_attributs[12].append(None)
    nb_genre = 3
if nb_act == 1:
    mv_attributs[11].append(None)
    mv_attributs[12].append(None)
    nb_genre = 3
if nb_act == 2:
    mv_attributs[12].append(None)
    nb_act = 3

award = html.find('div', id='titleAwardsRanks', class_='article highlighted')
test_rank = False
test_nb_oscar = False
test_win = False
test_nom = False


if award is not None:

    # movie rank
    if award.find('strong') is not None:
        strong = award.find('strong').text
        rank = scrap.clean_chars(strong)
        mv_attributs[13].append(rank)
        test_rank = True


    # oscars, wins and nominations
    if award.find_all('span', class_="awards-blurb") is not None:
        
        test_nb_oscar = False  #On en a besoin seulemnt dans la prmemière iteration de la boucle (après il n'y a plus de possibilité de trouver d'Oscar)
        
        for span in award.find_all('span', class_="awards-blurb"):
            
            
            # if there is/are oscar/s
            if span.find('b') is not None:            #Uniquement pour prendre l'Oscar
                nb_oscar = span.find('b').text
                nb_oscar = scrap.clean_chars(nb_oscar)
                mv_attributs[14].append(nb_oscar)
                test_nb_oscar = True

                #Encommentaire car inutile : On ne rentreras jamais dedans si on a touver un oscar avant 
                #                         car le span est celui d'oscar et non de win et nomination
                
                # print("new span : ", span)
                # length = len(span.text)
                # win = span.text[:length - 24]
                # win = scrap.clean_chars(win)
                # mv_attributs[15].append(win)
                # test_win = True              

                # print("spantext if1 : ",span.text)
                # nom = span.text[35:]
                # nom = scrap.clean_chars(nom)
                # mv_attributs[16].append(nom)
                # test_nom = True
                # print ('nom :', nom)
            
            else:               
                length = len(span.text)
                
                if length > 40:
                
                    print ("coucou")
                    win = span.text[:length - 24]  #On évite de prendre le nomination qu'on prend après
                    win = scrap.clean_chars(win)
                    mv_attributs[15].append(win)
                    test_win = True

                    nom = span.text[34:]  #On évite de prendre le win qu'on a déja
                    nom = scrap.clean_chars(nom)
                    mv_attributs[16].append(nom)
                    test_nom = True
                
                
                elif length <= 40 and length > 30:   
                    win = span.text[:length - 24]  #On évite de prendre le nomination qu'on prend après
                    win = scrap.clean_chars(win)
                    mv_attributs[15].append(win)
                    test_win = True

                    nom = span.text[14:]         #On évite de prendre le win qu'on a déja
                    nom = scrap.clean_chars(nom)
                    mv_attributs[16].append(nom)
                    test_nom = True
                    
                else:
                    win = None
                    nom = span.text
                    nom = scrap.clean_chars(nom)
                    mv_attributs[16].append(nom)
                    test_nom = True

if not test_rank:
    mv_attributs[13].append(0)
if not test_nb_oscar:
    mv_attributs[14].append(0)
if not test_win:
    mv_attributs[15].append(0)
if not test_nom:
    mv_attributs[16].append(0)

test_runtime=False
test_budget=False
test_gross=False

for div in html.find_all('div', class_="txt-block"):
    if div.find('h4', class_='inline') is not None:
        inline = div.find('h4', class_='inline').text
        # find the runtime in minutes
        if inline == "Runtime:":
            runtime = div.find('time').text
            runtime = scrap.clean_chars(runtime)
            mv_attributs[17].append(runtime)
            test_runtime = True

        # find the movie budget
        if inline == "Budget:":
            budget = div.text
            budget = scrap.clean_chars(budget)
            mv_attributs[18].append(budget)
            test_budget = True

        # find the movie worldwide gross
        if inline == "Cumulative Worldwide Gross:":
            gross = div.text
            gross = scrap.clean_chars(gross)
            mv_attributs[19].append(gross)
            test_gross = True

if not test_runtime:
    mv_attributs[17].append(None)
if not test_budget:
    mv_attributs[18].append(None)
if not test_gross:
    mv_attributs[19].append(None)

print (mv_attributs)