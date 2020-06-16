# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:49:34 2020
@author: Jules
"""

from warnings import warn
import bs4
import requests
import seaborn as sns; sns.set(style="ticks", color_codes=True)
def extraction_movie_data_from_link(link):
    '''
    Get some information from a movie link

    :param link http url: http url that point to the movie
    :return String list genres: list of the given movie genre
    :return int runtime: the given movie runtime in minutes
    :return int budget: the given movie budget
    :return int gross: the given movie worldwilde Gross

    '''

    genres = []

    page_link = "f'"+str(link)+"'"
    response = requests.get(page_link)
    html = bs4.BeautifulSoup(response.text, 'html.parser')

    #fin the movie title and the released date
    title = html.find('div', class_='title_wrapper')
    film_titre_date = title.h1.text
    #return(film_titre_date)

    if html.find('div', id='titleAwardsRanks') is not None:
        inline = html.find('h4', class_='inline').text

    #find the movie genres
    sub = html.find('div', class_="subtext")
    for balise in sub.find_all('a'):
        href = balise.get('href')
        if href != "/title/tt7286456/releaseinfo":
            genres.append(balise.text)

    for div in html.find_all('div', class_="txt-block"):
        if div.find('h4', class_='inline') is not None:
            inline = div.find('h4', class_='inline').text

            #find the runtime in minutes
            if inline == "Runtime:":
                runtime = div.text[9:]
                runtime = int(runtime[:-5])

            # find the movie budget
            if inline == "Budget:":
                budget = div.text[9:]
                if div.find('span', class_="attribute") is not None:
                    budget = budget[:11]
                budget = int(budget.replace(',', ''))

            # find the movie worldwide gross
            if inline == "Cumulative Worldwide Gross:":
                gross = div.text[30:]
                if div.find('span', class_="attribute") is not None:
                    gross = gross[:10]
                gross = int(gross.replace(',', ''))

    return genres, runtime, budget, gross



def warning_request(response, nb_requests):
    '''
    Throw a warning for any status codes different than 200

    :param string response:
    :return: void
    :rtype: None

    '''
    if response.status_code != 200:
        warn(': {}; Status code: {}'.format(nb_requests, response.status_code))