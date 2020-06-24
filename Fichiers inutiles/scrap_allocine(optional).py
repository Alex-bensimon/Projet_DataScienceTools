"""
Created on Sat Jun 13 22:16:49 2020
@author: Alex
"""
import bs4
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)

titre = []
nb_e = []
date = []
genre = []
duree = []
np = []
ns = []
realisateur = []
acteurs_principaux = []
classement = []
n = []

i=1
for i in range(10):
    page_number = i
    page_link = f'http://www.allocine.fr/film/meilleurs/boxoffice/?page={page_number}'
    response = requests.get(page_link)
    html = bs4.BeautifulSoup(response.text, 'html.parser')

    for div in html.find_all('div', attrs={'class':'card entity-card entity-card-list cf'}):
        film_title = div.find('a', {"class": "meta-title-link"})
        titre.append(film_title.text)
        date_sortie = div.find('span', {"class": "date"})
        if date_sortie != None:
            date.append(date_sortie.text)
        else:
            date.append(None)
        nb_entrees = div.find('div', {"class": "bo"})
        nb_e.append(int(nb_entrees.text.replace(' ','').replace('entrées','')))


        for cl in div.find_all('div', attrs={'class':"rating-item-content"}):
            type_note = cl.find('a', {"class": "xXx rating-title"})
            print(type_note.text)
            note = cl.find('span', {"class": "stareval-note"})
            if note != None:
                np.append(float(note.text.replace(',','.')))
            else:
                np.append(None)
            if note != None:
                ns.append(float(note.text.replace(',','.')))
            else:
                ns.append(None)
        """     
        note_presse = div.find('span', {"class": "stareval-note"})
        if note_presse != None:    
            np.append(float(note_presse.text.replace(',','.')))
        else:
            np.append(None)
        note_spect = div.find('span', {"class": "stareval-note"})
        if note_spect != None:        
            ns.append(float(note_spect.text.replace(',','.')))
        else:
            ns.append(None)
        """


df = pd.DataFrame({'Titre ':titre,'Date de sortie':date,
                        'Nombre entrées':nb_e,'Note presse':np,
                        'Note spect':ns})
print(note.text)
#print(df)
print(df.describe())


plt.figure(figsize=[10,10])
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.title('Correlations of the Features')
plt.show()
