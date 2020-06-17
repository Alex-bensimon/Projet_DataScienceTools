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

    # find the movie genres
    div = html.find('div', class_="subtext")
    for a in div.find_all('a'):
        title = a.get('title')
        #there is a balise title which we do not want
        if title is None:
            genres.append(a.text)

    award = html.find('div', id='titleAwardsRanks', class_='article highlighted')
    if award is not None:

        # movie rank
        if award.find('strong') is not None:
            strong = award.find('strong')
            rank = strong.text.translate(
                {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
            rank = int(rank)

        # oscars, wins and nominations
        if award.find_all('span', class_="awards-blurb") is not None:

            for span in award.find_all('span', class_="awards-blurb"):

                osc_bool = False
                # if there is/are oscar/s
                if span.find('b') is not None:
                    nb_oscar = span.find('b').text.translate(
                        {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
                    nb_oscar = int(nb_oscar)
                    osc_bool = True

                # if there is/are oscar/s
                elif osc_bool == True:
                    length = len(span.text)
                    win = span.text[:length - 24]
                    win = int(win.translate(
                        {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "}))

                    nom = span.text[32:]
                    nom = int(nom.translate(
                        {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "}))

                # if not
                else:
                    length = len(span.text)
                    win = span.text[:length - 24]
                    win = int(win.translate(
                        {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "}))

                    nom = span.text[15:]
                    nom = int(nom.translate(
                        {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "}))


    for div in html.find_all('div', class_="txt-block"):
        if div.find('h4', class_='inline') is not None:
            inline = div.find('h4', class_='inline').text
            # find the runtime in minutes
            if inline == "Runtime:":
                runtime = div.find('time')
                runtime = runtime.text.translate(
                    {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
                runtime = int(runtime)

            # find the movie budget
            if inline == "Budget:":
                budget = div.text
                budget = budget.translate(
                    {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
                budget = int(budget)

            # find the movie worldwide gross
            if inline == "Cumulative Worldwide Gross:":
                gross = div.text
                gross = gross.translate(
                    {ord(c): "" for c in "#/n:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,()[]{}\$£€& "})
                gross = int(gross)

    return genres,rank,nb_oscar,win,nom,runtime,budget,gross


def warning_request(response, nb_requests):
    '''
    Throw a warning for any status codes different than 200
    :param string response:
    :return: void
    :rtype: None
    '''
    if response.status_code != 200:
        warn(': {}; Status code: {}'.format(nb_requests, response.status_code))