# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:48:03 2020

@author: Alex
"""

import fonction_scraping_accueil as scrap
import fonction_traitement as trait
import definition_tab as dftab
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('movie_ratings_1980_2000_p10.csv')

print(df.describe())




