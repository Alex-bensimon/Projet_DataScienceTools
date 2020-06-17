# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:51:09 2020

@author: Victor HENRIO
"""


#scikit-learn
import sklearn
#classe pour standardisation
from sklearn.preprocessing import StandardScaler
#instanciation
sc = StandardScaler()   
#transformation – centrage-réduction
Z = sc.fit_transform(test)
print(Z)


#moyenne (pour chaque colonne, aucun sens pour toute la data frame)
print(np.mean(Z, axis=0))

#écart-type
print (np.nanstd(Z))

#%%

#classe pour l'ACP
from sklearn.decomposition import PCA
#instanciation
acp = PCA() 
acp.fit(Z) 

#affichage des paramètres

print("Pourcentage de variance expliquée : ") 
print(acp.explained_variance_ratio_) 
print("Composantes principales : ") 
print(acp.components_) 

#calculs
coord = acp.fit_transform(Z)
#nombre de composantes calculées
print(acp.n_components_) 

#%%
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

#%%

import matplotlib.pyplot as plt
#positionnement des individus dans le premier plan
fig, axes = plt.subplots(figsize=(12,12))
axes.set_xlim(-6,6) #même limites en abscisse
axes.set_ylim(-6,6) #et en ordonnée
#placement des étiquettes des observations
for i in range(n):
 plt.annotate(test.index[i],(coord[i,0],coord[i,1]))
#ajouter les axes
plt.plot([-6,6],[0,0],color='silver',linestyle='-',linewidth=1)
plt.plot([0,0],[-6,6],color='silver',linestyle='-',linewidth=1)
#affichage
plt.show()

#%%

#contribution des individus dans l'inertie totale
di = np.sum(Z**2,axis=1)
print(pd.DataFrame({'ID':test.index,'d_i':di}))

#%%

#qualité de représentation des individus - COS2
cos2 = coord**2
for j in range(p):
 cos2[:,j] = cos2[:,j]/di
print(pd.DataFrame({'id':test.index,'COS2_1':cos2[:,0],'COS2_2':cos2[:,1]}))


#%%

#contributions aux axes
ctr = coord**2
for j in range(p):
 ctr[:,j] = ctr[:,j]/(n*eigval[j])

print(pd.DataFrame({'id':test.index,'CTR_1':ctr[:,0],'CTR_2':ctr[:,1]}))


#%%

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


#%%

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

#%%

#cosinus carré des variables
cos2var = corvar**2
print(pd.DataFrame({'id':test.columns,'COS2_1':cos2var[:,0],'COS2_2':cos2var[:,1]}))


#%%

#contributions
ctrvar = cos2var
for k in range(p):
 ctrvar[:,k] = ctrvar[:,k]/eigval[k]
#on n'affiche que pour les deux premiers axes
print(pd.DataFrame({'id':test.columns,'CTR_1':ctrvar[:,0],'CTR_2':ctrvar[:,1]}))