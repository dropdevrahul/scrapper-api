from django.urls import path
from . import views

urlpatterns = [
        path('movie/<int:movie_id>/watchlist', views.UserWatchListMoviesView.as_view(), name='movie_watchlist'),
        path('movie/<int:movie_id>/watched', views.UserWatchedMoviesView.as_view(), name='movie_watched'),
        path('movies/watchlist', views.UserWatchListMoviesListView.as_view(), name='get_movies_watchlist'),
        path('movies/watched', views.UserWatchedMoviesListView.as_view(), name='get_movies_watched'),
]
