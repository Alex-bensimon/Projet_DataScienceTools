import numpy as np 
import pandas as pd


def actors_to_num(csv_name):

    df = pd.read_csv(csv_name)

    acteurs = []
    acteurs = df['stars']
    temp = []
    index_acteurs = []

    index = 0
    for act in acteurs:
        if act in temp:
            index_acteurs.append(temp.index(act))
        else: 
            temp.append(act)
            index_acteurs.append(index)
            index += 1

    #table_corres_df = np.array([index_acteurs, temp])
    len_temp = []
    i = 0
    for i in range(len(temp)):
        len_temp.append(i)
    print(len_temp)
    df2 = pd.DataFrame({'Index': len_temp,'Acteur': temp})
    df2 = df2.set_index('Index')
    print(df2)
    df2.to_csv('table_correspondance_acteurs.csv')


actors_to_num('movie_ratings.csv')
