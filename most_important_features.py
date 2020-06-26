# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 00:23:12 2020

@author: Alex
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import fonction_traitement as trait
import actors_labelisation as act
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.linear_model import LinearRegression

movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_1980_2020_final.csv')

movie_ratings = trait.clean_dataframe(movie_ratings,3,4,5,6,7,8)

movie_ratings = movie_ratings.drop(["win"],axis=1)
movie_ratings = movie_ratings.drop(["nom"],axis=1)
movie_ratings = movie_ratings.drop(["runtime"],axis=1)
movie_ratings = movie_ratings.drop(["metascore"],axis=1)
movie_ratings = movie_ratings.drop(["votes"],axis=1)

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']

# Set seed for reproducibility
SEED = 1
# Split dataset into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.3,random_state=SEED)

# Instantiate a random forests regressor 'rf' 400 estimators
rf = RandomForestRegressor(n_estimators=400,
min_samples_leaf=0.12,random_state=SEED)
# Fit 'rf' to the training set
rf.fit(X_train, y_train)
# Predict the test set labels 'y_pred'
y_pred = rf.predict(X_test)
print(y_pred)
# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred)**(1/2)
# Print the test set RMSE
print('Test set RMSE of rf: {:.2f}'.format(rmse_test))

# Create a pd.Series of features importances
importances_rf = pd.Series(rf.feature_importances_, index = X.columns)
# Sort importances_rf
sorted_importances_rf = importances_rf.sort_values()
# Make a horizontal bar plot
sorted_importances_rf.plot(kind='barh', color='lightgreen'); plt.show()