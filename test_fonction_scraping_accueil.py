import unittest
from fonction_scraping_accueil import years_loop,nb_page,clean_chars,clean_title


class Test_fonction_scraping_accueil(unittest.TestCase):
    def test_years_loop(self):
        # Given
        n = 10
        expected_output = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012
                            , 2011]
        # When
        output = years_loop(n)
        # Then
        self.assertEqual(expected_output, output)

    def test_nb_page(self):
        # Given
        n = 4
        expected_output = [0,51,101,151]
        # When
        output = nb_page(n)
        # Then
        self.assertEqual(expected_output, output)

    def test_clean_chars(self):
        # Given
        chain = "fhuegu12i gztr{# 345"
        expected_output = "12345"
        # When
        output = clean_chars(chain)
        # Then
        self.assertEqual(expected_output, output)

    def test_clean_title(self):
        # Given
        chain = "The Good, the Bad and the Ugly"
        expected_output = "The Good the Bad and the Ugly"
        # When
        output = clean_title(chain)
        # Then
        self.assertEqual(expected_output, output)



