# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:21:56 2020

@author: Alex
"""

#%%
import math
import pandas as pd

movie_ratings = pd.read_csv('movie_ratings_1980_2000_p10.csv')
i = 0 
for genre in movie_ratings['genres2']:
    string_test = isinstance(genre, str)
    if string_test is False:
        test = math.isnan(float(genre))
        if test is True:
            movie_ratings['genres2'][i] = movie_ratings['genres1'][i]
        else:
            pass
    i += 1

i = 0 
for genre in movie_ratings['genres3']:
    string_test = isinstance(genre, str)
    if string_test is False:
        test = math.isnan(float(genre))
        if test is True:
            movie_ratings['genres3'][i] = movie_ratings['genres2'][i]
        else:
            pass
    i += 1
    
print(movie_ratings['genres1'])
print(movie_ratings['genres2'])
print(movie_ratings['genres3'])

#%%
import math
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder


df = movie_ratings
df = df.dropna()

print(movie_ratings.shape)
print(df.shape)

row1 = 8
row2 = 9
row3 = 10

first_part = []
second_part = []
third_part = []

y = df.iloc[:,row1]
y = y.append(df.iloc[:,row2])
y = y.append(df.iloc[:,row3])

y = y.reset_index()
y = y.drop(["index"],axis=1)

tier = int(len(y)/3)
tier2 = int((len(y)/3)*2)

encoder = LabelEncoder()
normal_y = encoder.fit_transform(y)

print(y.shape)

i = 0
while i < len(normal_y):
    if i < tier:
        first_part.append(normal_y[i])
        i += 1
    elif i >= tier and i < tier2:
        second_part.append(normal_y[i])
        i += 1
    elif i >= tier2:
        third_part.append(normal_y[i])
        i += 1

df_test = pd.DataFrame({'new_genre1': first_part})

#ovie_ratings['genres1'] = movie_ratings['genres1'].replace(first_part)
movie_ratings['genres1'] = first_part
#df.loc[['viper', 'sidewinder'], ['shield']] = 50
#movie_ratings["new_genre2"] = second_part
#ovie_ratings["new_genre3"] = third_part

print("---"*30)
print(movie_ratings['genres1'])
#print(movie_ratings['new_genres1'])
print("---"*30)





