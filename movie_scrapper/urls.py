from django.conf.urls import url
from .views import ScrapperView, MoviesView

urlpatterns = [
    url(r'scrape', ScrapperView.as_view()),
    url(r'movies', MoviesView.as_view()),
]
