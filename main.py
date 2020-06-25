# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:50:08 2020

@author: Victor HENRIO
"""

import os
import pandas as pd
#from fonction_analyse import launch_prediction


def main(): 
    
    choice = 0
    test = False
    
    while test == False :  
        
        print ("\n ##########  Bienvenue chez Remi_Stream ########## \n")
        print ("Que souhaitez-vous faire :")
        print ("1 - Scraper les données de IMDB")
        print ("2 - Faire une analyse en compansante principale sur des données déjà scrapées")
        print ("3 - Aplliquer du machine Learning et faire des trucs de DINGUES !!!")
        print ("4 - J'en ai déjà marre, je me casse...")
        
        choice = input()
        
        
        if int(choice) == 4:
            return None
        else :
            test = True
         
    print("\n\n#################################################\n#################################################\n\n")
    if int(choice) == 1:
        import fonction_scraping_total as scrap_tot
        print("Nous allons scraper le site IMDB, mais pour ça nous devons connaitre plusieurs informations: \n")
        print("- Combien d'années à partir de 2020 voulez-vous scraper ?")
        nb_years = int(input())
        print("- Combien de pages par année voulez-vous scraper ?")
        nb_pages= int(input())     
        scrap_tot.scraping_total(nb_years, nb_pages)
    
    if int(choice)==2:
        import ACP_film as acp
        print("Vous allez décrouvrir les différentes données que nous avons pu obtenir graçe à 15000 films entre 2020 et 1980:")
        acp.ACP_film()
    
    if int(choice) == 3:
        import fonction_analyse as analy
        print("Nous allons débuter le machine learning")
        analy.launch_prediction()
        
main()
        