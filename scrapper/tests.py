import unittest
from .scrapper import get_movies_list, get_movie_details


class TestScrapper(unittest.TestCase):

    def test_scrap_movies_list_without_details(self):
        test_url = 'https://www.imdb.com/chart/top/'
        movies_links = get_movies_list(test_url)
        self.assertTrue(len(movies_links) > 0)
        for item in movies_links:
            self.assertTrue(item.startswith(r'/title'))

    def test_scrap_movie_details(self):
        test_url = '/title/tt0111161/'
        movie_detail = get_movie_details(test_url)
        self.assertEqual(movie_detail.title, 'The Shawshank Redemption (1994)')
        self.assertEqual(movie_detail.url, 'https://imdb.com/title/tt0111161/')
        self.assertTrue(movie_detail.storyline)
