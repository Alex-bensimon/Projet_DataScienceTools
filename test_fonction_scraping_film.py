import unittest
from fonction_scraping_film import extraction_movie_data_from_link

class Test_fonction_scraping_film(unittest.TestCase):
    def test_extraction_movie_data_from_link(self):
        # Given
        link = 'https://www.imdb.com/title/tt7286456/?ref_=hm_fanfav_tt_2_pd_fp1'
        names = []  # 0
        years = []  # 1
        imdb_ratings = []  # 2
        metascores = []  # 3
        votes = []  # 4
        categories = []  # 5
        mv_pages = []  # 6
        genre1 = []  # 7
        genre2 = []  # 8
        genre3 = []  # 9
        stars1 = []  # 10
        stars2 = []  # 11
        stars3 = []  # 12
        rank = []  # 13
        nb_oscar = []  # 14
        win = []  # 15
        nom = []  # 16
        runtime = []  # 17
        budget = []  # 18
        gross = []  # 19
        mv_attributs = names, years, imdb_ratings, metascores, votes, categories, mv_pages, genre1, genre2, genre3, stars1, stars2, stars3, rank, nb_oscar, win, nom, runtime, budget, gross

        expected_output_genres = [['Crime'], ['Drama'], ['Thriller']]
        expected_output_stars = [['Joaquin Phoenix'], ['Robert De Niro'], ['Zazie Beetz']]
        expected_output_rank = ['56']
        expected_output_oscars = ['2']
        expected_output_wins = ['94']
        expected_output_nomination = ['200']
        expected_output_budget = ['55000000']
        expected_output_gross = ['1074251311']
        expected_output_runtime = ['122']

        # When
        output = extraction_movie_data_from_link(link, mv_attributs)

        # Then
        for i in range(3):
            self.assertEqual(expected_output_genres[i], output[7 + i])
            self.assertEqual(expected_output_stars[i], output[10 + i])
        self.assertEqual(expected_output_rank, output[13])
        self.assertEqual(expected_output_oscars, output[14])
        self.assertEqual(expected_output_wins, output[15])
        self.assertEqual(expected_output_nomination, output[16])
        self.assertEqual(expected_output_runtime, output[17])
        self.assertEqual(expected_output_budget, output[18])
        self.assertEqual(expected_output_gross, output[19])
