import collections

from bs4 import BeautifulSoup
import requests

MovieDetail = collections.namedtuple('MovieDetail', 'title storyline url')

def get_movie_details(relative_movie_url):
    movie_url = 'https://imdb.com' + relative_movie_url
    response = requests.get(movie_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        movie_title = soup.select('.title_wrapper h1')[0].text.strip()
        movie_title = movie_title.replace(u'\xa0', u' ')
        movie_storyline = soup.select('#titleStoryLine .inline.canwrap span')[0].text.strip()
        return MovieDetail(title=movie_title, storyline=movie_storyline, url=movie_url)

def get_movies_list(movie_list_url):
    response = requests.get(movie_list_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        trs = soup.select('.lister .lister-list tr')
        movies_links = [item.find('a')['href'] for item in trs]
        return movies_links
