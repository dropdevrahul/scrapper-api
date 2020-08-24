import logging
from scrapper.scrapper import get_movie_details, get_movies_list
from .models import MovieDetail
import time
logger = logging.getLogger(__name__)


def scrap_and_store_movies_details(movies_list_url, user):
    """
        scrapes and stores movie details for the given movies_list_url max 100 movies are scrapped at a time
        Attributes:
        ----------
        movies_list_url url:
                movie list url from IMDB domain
        user user_app.ApiUser:
                Logged in Django User
    """
    movie_links = get_movies_list(movies_list_url)
    count = 0
    for link in movie_links:
        try:
            movie_detail = get_movie_details(link)
            MovieDetail.objects.update_or_create(title=movie_detail.title, defaults={
                    'storyline': movie_detail.storyline,
                    'title': movie_detail.title,
                    'url': movie_detail.url,
                })
            count += 1
            time.sleep(0.1)
            logger.info("Scrapping successful for movie link : {}".format(link))
        except Exception as e:
            logger.error('Scrapping failed for movie link : {}'.format(link))
            logger.error(str(e), exc_info=True)
            continue

    return count

