# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:05:34 2020

@author: Alex
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder

row1 = 7
row2 = 8
row3 = 9

df = pd.read_csv('movie_ratings_1980_2000_p10.csv')

first_part = []
second_part = []
third_part = []

y = df.iloc[:,row1]
y = y.append(df.iloc[:,row2])
y = y.append(df.iloc[:,row3])

y = y.reset_index()
y = y.drop(["index"],axis=1)

print(y)

tier = int(len(y)/3)
tier2 = int((len(y)/3)*2)


encoder = LabelEncoder()
normal_y = encoder.fit_transform(y)
# encoder = LabelBinarizer()
# test = encoder.fit_transform(y)
print(normal_y)
i = 0
while i < len(normal_y):
    if i <= tier:
        first_part.append(normal_y[i])
        i += 1
    elif i >= tier and i < tier2:
        second_part.append(normal_y[i])
        i += 1
    elif i >= tier2:
        third_part.append(normal_y[i])
        i += 1
        
print(row1)
df[row1] = first_part
df[row2] = second_part
df[row3] = third_part

print("---"*30)
print(df)
print("---"*30)

