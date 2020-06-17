# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:49:34 2020
@author: Jules
"""

from warnings import warn
import bs4
import requests
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import fonction_scraping as scrap

#def extraction_movie_data_from_link(link):
def extraction_movie_data_from_link(link, mv_attributs):
    '''
    Get some information from a movie link
    :param link http url: http url that point to the movie
    :return String list genres: list of the given movie genre
    :return String list stars: list of the given movie stars
    :return int rank: the given movie rank in IMDB
    :return int nb_oscar: the number of oscars won by the movie
    :return int win: the number of nomination wins
    :return int nom: the number of nominations
    :return int runtime: the given movie runtime in minutes
    :return int budget: the given movie budget
    :return int gross: the given movie worldwilde Gross
    '''


    page_link = link
    response = requests.get(page_link)
    html = bs4.BeautifulSoup(response.text, 'html.parser')

    #get the movie genres
    div = html.find('div', class_="subtext")
    for a in div.find_all('a'):
        title = a.get('title')
        #there is a balise title which we do not want
        if title is None:
            mv_attributs[7].append(a.text)

    #get the stars acting in the movie
    stars = []
    for credit in html.find_all('div', class_='credit_summary_item'):
        inline = credit.h4.text
        if inline == "Stars:":
            for a in credit.find_all('a'):
                href = a.get('href')
                if href != "fullcredits/":
                    mv_attributs[8].append(a.text)

    award = html.find('div', id='titleAwardsRanks', class_='article highlighted')
    if award is not None:

        # movie rank
        if award.find('strong') is not None:
            strong = award.find('strong').strong.text
            rank = scrap.clean_chars(strong)
            mv_attributs[9].append(rank)

        # oscars, wins and nominations
        if award.find_all('span', class_="awards-blurb") is not None:

            for span in award.find_all('span', class_="awards-blurb"):

                osc_bool = False
                # if there is/are oscar/s
                if span.find('b') is not None:
                    print("1####")
                    nb_oscar = span.find('b').text
                    nb_oscar = scrap.clean_chars(nb_oscar)
                    mv_attributs[9].append(rank)
                    osc_bool = True

                # if there is/are oscar/s
                elif osc_bool == True:
                    print("2####")
                    length = len(span.text)
                    win = span.text[:length - 24]
                    win = scrap.clean_chars(win)
                    mv_attributs[11].append(win)

                    nom = span.text[32:]
                    nom = scrap.clean_chars(nom)
                    mv_attributs[12].append(nom)
                # if not
                else:
                    print("3####")
                    length = len(span.text)
                    
                    if length > 30 :
                    
                        win = span.text[:length - 24]
                        win = scrap.clean_chars(win)
                        mv_attributs[11].append(win)
    
                        nom = span.text[15:]
                        nom = scrap.clean_chars(nom)
                        mv_attributs[12].append(nom)
                        
                    else :
                        win = None
                            
                        nom = span.text
                        nom = scrap.clean_chars(nom)
                        mv_attributs[12].append(nom)

    for div in html.find_all('div', class_="txt-block"):
        if div.find('h4', class_='inline') is not None:
            inline = div.find('h4', class_='inline').text
            # find the runtime in minutes
            if inline == "Runtime:":
                runtime = div.find('time').text
                runtime = scrap.clean_chars(runtime)
                mv_attributs[13].append(runtime)

            # find the movie budget
            if inline == "Budget:":
                budget = div.text
                budget = scrap.clean_chars(budget)
                mv_attributs[14].append(budget)

            # find the movie worldwide gross
            if inline == "Cumulative Worldwide Gross:":
                gross = div.text
                gross = scrap.clean_chars(gross)
                mv_attributs[15].append(gross)
                
    return mv_attributs

def caca():
    print(1)

def warning_request(response, nb_requests):
    '''
    Throw a warning for any status codes different than 200
    :param string response:
    :return: void
    :rtype: None
    '''
    if response.status_code != 200:
        warn(': {}; Status code: {}'.format(nb_requests, response.status_code))


#extraction_movie_data_from_link(f"https://www.imdb.com/title/tt7286456/?ref_=hm_fanfav_tt_2_pd_fp1")