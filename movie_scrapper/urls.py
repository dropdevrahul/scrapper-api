from django.urls import path
from .views import ScrapperView, MoviesView

urlpatterns = [
    path('scrape', ScrapperView.as_view()),
    path('movies', MoviesView.as_view()),
]
