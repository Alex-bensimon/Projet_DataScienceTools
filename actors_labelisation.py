# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:05:34 2020

@author: Alex
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder


df = pd.read_csv('movie_ratings.csv')
y = []

first_part = []
second_part = []
third_part = []

y = df['stars1']
y = y.append(df['stars2'])
y = y.append(df['stars3'])

tier = int(len(y)/3)
tier2 = int((len(y)/3)*2)

print(tier)
print(tier2)

encoder = LabelEncoder()
test = encoder.fit_transform(y)

print(test)

i = 0
while i < len(y):
    if i < tier:
        first_part.append(y[i])
        print(first_part[i])
        i += 1
    elif i >= tier and i < tier2:
        second_part.append(y[i])
        print(second_part[i])
        i += 1
    elif i >= tier2:
        third_part.append(y[i])
        print(third_part[i])
        i += 1
    
print(first_part)
print(second_part)
print(third_part)


"""
#encoder.inverse_transform(np.array([0, 0, 2]))

encoder = LabelBinarizer()
test2 = encoder.fit_transform(y)

print(test2)
"""