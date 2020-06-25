# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 08:19:10 2020
@author: Victor HENRIO
"""


import fonction_scraping_accueil as scrap
import fonction_traitement as trait
import definition_tab as dftab
import API as api
import pandas as pd
import numpy as np

import fonction_traitement as trait
import actors_labelisation as act
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder


def ACP_film(movie_ratings):   
    
    import numpy as np
    
    #movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')
    
    #movie_ratings = movie_ratings.drop(["Unnamed: 0"],axis=1)
    movie_ratings = movie_ratings.set_index('movie')
    movie_ratings = movie_ratings.drop(["mv_page"],axis=1)
    movie_ratings = movie_ratings.drop(["rank"],axis=1)
    movie_ratings['years'] = movie_ratings['year'].astype(str).str[:4]
    movie_ratings = movie_ratings.drop(["year"],axis=1)
    movie_ratings['runtime'] = movie_ratings['runtime'].fillna(movie_ratings['runtime'].mean())
    movie_ratings = trait.replace_metascore(movie_ratings)
    movie_ratings = trait.add_0_win_nom(movie_ratings)
    movie_ratings['budget'] = movie_ratings['budget'].fillna(movie_ratings['budget'].mean())
    movie_ratings['gross'] = movie_ratings['gross'].fillna(movie_ratings['gross'].mean())
    movie_ratings['category'] = movie_ratings['category'].replace({"R":1}).replace({"PG-13":3}).replace({"PG":2})
    movie_ratings = act.imputation_previous_value(movie_ratings)
    movie_ratings = movie_ratings.dropna()
    
    
    # y_years = movie_ratings.iloc[:,16]
    # encoder = LabelEncoder()
    # normal_y = encoder.fit_transform(y_years)
    # movie_ratings['years'] = normal_y
    
    print(movie_ratings.info())
    


    movie_ratings = act.labelisation(movie_ratings,4,5,6,7,8,9)

    
    #movie_ratings = trait.clean_dataframe(movie_ratings)
    
    
    print(movie_ratings.info())
    

    
    test = movie_ratings
    #Partie Analyse 
    
    #scikit-learn
    import sklearn
    #classe pour standardisation
    from sklearn.preprocessing import StandardScaler
    #instanciation
    sc = StandardScaler()   
    #transformation – centrage-réduction
    Z = sc.fit_transform(test)
    
    #écart-type
    print (np.nanstd(Z))
    

    
    #classe pour l'ACP
    from sklearn.decomposition import PCA
    #instanciation
    acp = PCA() 
    acp.fit(Z) 
    
    #affichage des paramètres
    
    print("Pourcentage de variance expliquée : ") 
    print(acp.explained_variance_ratio_) 
    #print("Composantes principales : ") 
    #print(acp.components_) 
    
    #calculs
    coord = acp.fit_transform(Z)
    #nombre de composantes calculées
    #print(acp.n_components_) 
    
    
     # 0   imdb_ratings  10629 non-null  float64
     # 1   metascore     10629 non-null  float64
     # 2   votes         10629 non-null  float64
     # 3   category      10629 non-null  float64
     # 4   genres1       10629 non-null  object 
     # 5   genres2       10629 non-null  object 
     # 6   genres3       10629 non-null  object 
     # 7   stars1        10629 non-null  object 
     # 8   stars2        10629 non-null  object 
     # 9   stars3        10629 non-null  object 
     # 10  nb_oscar      10629 non-null  float64
     # 11  win           10629 non-null  float64
     # 12  nom           10629 non-null  float64
     # 13  runtime       10629 non-null  float64
     # 14  budget        10629 non-null  float64
     # 15  gross         10629 non-null  float64
     # 16  years         10629 non-null  object 
    
    
    n = test.shape[0] 
    p = test.shape[1] 
    
    #variance expliquée pour avoir des infos sur les valeurs propres (première est toujours supèrieur à1)
    eigval = (n-1)/n*acp.explained_variance_ 
    print(eigval)
    
    
    #proportion de variance expliquée
    print(acp.explained_variance_ratio_)
    
    #scree plot : Critère de coude
    import matplotlib.pyplot as plt
    
    plt.plot(np.arange(1,p+1),eigval)
    plt.title("Scree plot")
    plt.ylabel("Eigen values")
    plt.xlabel("Factor number")
    plt.show()
    
    #cumul de variance expliquée
    plt.plot(np.arange(1,p+1),np.cumsum(acp.explained_variance_ratio_))
    plt.title("Explained variance vs. # of factors")
    plt.ylabel("Cumsum explained variance ratio")
    plt.xlabel("Factor number")
    plt.show()
    
    ''' Affichage des film en fonction des Axes Factoriel
    
    import matplotlib.pyplot as plt
    #positionnement des individus dans le premier plan
    fig, axes = plt.subplots(figsize=(150,150))
    axes.set_xlim(-6,6) #même limites en abscisse
    axes.set_ylim(-6,6) #et en ordonnée
    #placement des étiquettes des observations
    for i in range(n):
        #print("note:",movie_ratings["imdb_ratings"][i])
        red = ((-255/10) * (movie_ratings["imdb_ratings"][i])+255)/255
        #print("red :", red)
        green = ((255/10) * (movie_ratings["imdb_ratings"][i]))/255
        #print("green", green)
        blue = 0
        plt.annotate(test.index[i],(coord[i,0],coord[i,1]),color=(red,green,blue))
    #ajouter les axes
    plt.plot([-6,6],[0,0],color='silver',linestyle='-',linewidth=1)
    plt.plot([0,0],[-6,6],color='silver',linestyle='-',linewidth=1)
    #affichage
    plt.show()
    
    '''

    import numpy as np
    
    #contribution des individus dans l'inertie totale
    di = np.sum(Z**2,axis=1)
    print(pd.DataFrame({'ID':test.index,'d_i':di}))
    

    
    #qualité de représentation des individus - COS2
    cos2 = coord**2
    for j in range(p):
     cos2[:,j] = cos2[:,j]/di
    print(pd.DataFrame({'id':test.index,'COS2_1':cos2[:,0],'COS2_2':cos2[:,1]}))
    
    

    
    #contributions aux axes
    ctr = coord**2
    for j in range(p):
     ctr[:,j] = ctr[:,j]/(n*eigval[j])
    
    print(pd.DataFrame({'id':test.index,'CTR_1':ctr[:,0],'CTR_2':ctr[:,1]}))
    

    
    #racine carrée des valeurs propres
    sqrt_eigval = np.sqrt(eigval)
    #corrélation des variables avec les axes
    corvar = np.zeros((p,p))
    for k in range(p):
     corvar[:,k] = acp.components_[k,:] * sqrt_eigval[k]
    
    #afficher la matrice des corrélations variables x facteurs
    print(corvar)
    
    
    #on affiche pour les deux premiers axes
    print(pd.DataFrame({'id':test.columns,'COR_1':corvar[:,0],'COR_2':corvar[:,1]}))
    

    
    #cercle des corrélations
    fig, axes = plt.subplots(figsize=(8,8))
    axes.set_xlim(-1,1)
    axes.set_ylim(-1,1)
    #affichage des étiquettes (noms des variables)
    for j in range(p):
     plt.annotate(test.columns[j],(corvar[j,0],corvar[j,1]))
    
    #ajouter les axes
    plt.plot([-1,1],[0,0],color='silver',linestyle='-',linewidth=1)
    plt.plot([0,0],[-1,1],color='silver',linestyle='-',linewidth=1)
    #ajouter un cercle
    cercle = plt.Circle((0,0),1,color='blue',fill=False)
    axes.add_artist(cercle)
    #affichage
    plt.show()
    

    #cosinus carré des variables
    cos2var = corvar**2
    print(pd.DataFrame({'id':test.columns,'COS2_1':cos2var[:,0],'COS2_2':cos2var[:,1]}))
    
    

    
    #contributions
    ctrvar = cos2var
    for k in range(p):
     ctrvar[:,k] = ctrvar[:,k]/eigval[k]
    #on n'affiche que pour les deux premiers axes
    print(pd.DataFrame({'id':test.columns,'CTR_1':ctrvar[:,0],'CTR_2':ctrvar[:,1]}))