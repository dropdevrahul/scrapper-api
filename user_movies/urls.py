from django.conf.urls import url
from .views import UserWatchedMoviesView, UserWatchListMoviesView

urlpatterns = [
    url(r'movies/watchlist', UserWatchListMoviesView.as_view()),
    url(r'movies/watched', UserWatchedMoviesView.as_view()),
]
