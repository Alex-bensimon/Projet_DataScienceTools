# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:05:34 2020

@author: Alex
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder

def labelisation_attributs(movie_ratings,row1,row2,row3):
    
    df = movie_ratings
    
    first_part = []
    second_part = []
    third_part = []
    
    y = df[row1]
    y = y.append(df[row2])
    y = y.append(df[row3])
    
    y = y.reset_index()
    y=y.drop(["index"],axis=1)
    
    print(y)
    
    tier = int(len(y)/3)
    tier2 = int((len(y)/3)*2)
    
    
    encoder = LabelBinarizer()
    normal_y = encoder.fit_transform(y)
    # encoder = LabelEncoder()
    # test = encoder.fit_transform(y)
    
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
    
        
    print(first_part)
    print(second_part)
    print(third_part)
    
    
    """
    #encoder.inverse_transform(np.array([0, 0, 2]))
    
    encoder = LabelBinarizer()
    test2 = encoder.fit_transform(y)
    
    print(test2)
    """