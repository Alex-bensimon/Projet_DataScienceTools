import unittest
from actors_labelisation import imputation_previous_value,labelisation
import fonction_traitement as trait
import pandas as pd
from numpy import nan as Nan
import numpy as np
#dataframes building for tests
movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')
movie_ratings = trait.clean_dataframe(movie_ratings,3,4,5,6,7,8)

movie_ratings = movie_ratings[:3]
list_nan = []
for x in range(len(movie_ratings.columns)):
    if movie_ratings.columns[x] == 'genres1':
        list_nan.append('TEST')
    else:
        list_nan.append(Nan)

columns = movie_ratings.columns.values.tolist()
s2 = pd.Series(list_nan, index=columns)
movie_ratings_nan = movie_ratings.append(s2,ignore_index=True)


class Test_actors_labelisation(unittest.TestCase):
    def test_imputation_previous_value(self):
        # Given
        n = movie_ratings_nan

        #movie_ratings_nan['genres2'][3] = 'TEST'
        #movie_ratings_nan['genres3'][3] = 'TEST'
        expected_output1 = 'TEST'
        expected_output2 = 'TEST'
        # When
        output1 = imputation_previous_value(n)['genres2'][3]
        output2 = imputation_previous_value(n)['genres3'][3]

        # Then
        self.assertEqual(expected_output1, output1)
        self.assertEqual(expected_output2, output2)

