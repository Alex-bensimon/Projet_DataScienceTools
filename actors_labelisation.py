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
for i in range(tier):
    print("zu")



"""
#encoder.inverse_transform(np.array([0, 0, 2]))

encoder = LabelBinarizer()
test2 = encoder.fit_transform(y)

print(test2)
"""