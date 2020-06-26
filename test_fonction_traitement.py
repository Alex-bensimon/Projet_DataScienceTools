import unittest
from fonction_traitement import delete_raws_nan,replace_metascore,clean_dataframe,add_0_win_nom
import fonction_traitement as trait
import pandas as pd
from numpy import nan as Nan
movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')
movie_ratings = trait.clean_dataframe(movie_ratings,3,4,5,6,7,8)

movie_ratings = movie_ratings[:3]
list_nan = []
list_win = []
list_imdb_ratings = []
for x in range(len(movie_ratings.columns)):
    list_nan.append(Nan)
    if movie_ratings.columns[x] == 'genres1':
        list_win.append('TEST')
        list_imdb_ratings.append(Nan)
    elif movie_ratings.columns[x] == 'imdb_ratings':
        list_imdb_ratings.append(5)
        list_win.append(Nan)
    else:
        list_win.append(Nan)
        list_imdb_ratings.append(Nan)

columns = movie_ratings.columns.values.tolist()

s2 = pd.Series(list_nan, index=columns)
s3 = pd.Series(list_win, index=columns)
s4 = pd.Series(list_imdb_ratings, index=columns)

movie_ratings_nan = movie_ratings.append(s2,ignore_index=True)
movie_ratings_win = movie_ratings.append(s3,ignore_index=True)
movie_ratings_imdb_rating = movie_ratings.append(s4,ignore_index=True)
#print(movie_ratings_nan)

class Test_fonction_traitement(unittest.TestCase):
    def test_delete_raws_nan(self):
        # Given
        n = movie_ratings_nan
        expected_output = 3
        # When
        output = len(delete_raws_nan(n).index)
        # Then
        #On test ici uniquement que la ligne a bien ete supprimée, donc test sur nombre de row
        self.assertEqual(expected_output, output)

    def test_replace_metascore(self):
        # Given
        n = movie_ratings_imdb_rating
        expected_output = 50.0
        # When
        output = replace_metascore(n)['metascore'][3]

        # Then
        #Est ce que la valeur de la colonne metascore a bien ete modifiée
        self.assertEqual(expected_output, output)

    def test_add_0_win_nom(self):
        # Given
        n = movie_ratings_win
        expected_output = 0
        # When
        output = add_0_win_nom(n)['nom'][3]

        # Then
        # Est ce que la valeur de la colonne nomination a bien ete mis à 0
        self.assertEqual(expected_output, output)


