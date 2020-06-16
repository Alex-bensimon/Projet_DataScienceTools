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
nb_entrees = []
date_sortie = []
genre = []
duree = []
note_spect = []
note_presse = []
realisateur = []
acteurs_principaux = []
classement = []
n = []

pages = [1,2,3,4,5]
page = 1

for page in pages:
   
    page_link = f'http://www.allocine.fr/film/meilleurs/boxoffice/?page={page}'
    
    response = requests.get(page_link)
    
    html = bs4.BeautifulSoup(response.text, 'html.parser')
    
    mv_containers = html.find_all('div', attrs={'class':'card entity-card entity-card-list cf'})
    
    for container in mv_containers:    
        
        if container.find('div', class_ = 'ratings-metascore') is not None:
              
            #Scrap the title 
            film_title = container.find('a', {"class": "meta-title-link"})
            titre.append(film_title.text)
            
            #Scrap the release date
            date_sortie = container.find('span', {"class": "date"})           
            if date_sortie != None:
                date_sortie.append(date_sortie.text)  # peu interressant car date_reprise != date sortie
            else:
                date_sortie.append(None) 
            
            #Scrap number of admission
            nb_entrees = container.find('div', {"class": "bo"})
            nb_entrees.append(int(nb_entrees.text.replace(' ','').replace('entrées','')))
            
            #Srap the ratting
            rating_container = container.find_all('div', attrs={'class':"rating-item-content"})
    
            for section in rating_container:
                
                note = section.find('span', {"class": "stareval-note"}).text
                
                
                if note != None:    
                    note.append((note.text.replace(',','.')))
                else:
                    note_presse.append(None)
    
                if note != None:        
                    note_spect.append((note.text.replace(',','.')))
                else:
                    note_spect.append(None)
                    
                    
                    
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
    
    
df = pd.DataFrame({'Titre ':titre,'Date de sortie':date_sortie,
                        'Nombre entrées':nb_entrees,'Note presse':note_presse })
print(note)
#print(df)
print(df.describe())


plt.figure(figsize=[10,10])
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.title('Correlations of the Features')
plt.show()
