import unittest
from API import API_search_director
import fonction_traitement as trait
import pandas as pd
from numpy import nan as Nan
"""
movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')
movie_ratings = trait.clean_dataframe(movie_ratings,3,4,5,6,7,8)

movie_ratings = movie_ratings[:1]
print(API_search_director(movie_ratings)["director"][0])

IMPOSSIBLE DE TESTER CAR PB DANS LE CODE?
TypeError: 'int' object is not subscriptable
class Test_fonction_traitement(unittest.TestCase):
    def test_API_search_director(self):
        # Given
        n = movie_ratings
        expected_output = "George Miller"
        # When
        output = API_search_director(n)["director"][0]
        # Then
        self.assertEqual(expected_output, output)
"""


