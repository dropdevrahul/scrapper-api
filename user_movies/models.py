from django.db import models
from movie_scrapper.models import MovieDetail
from user_app.models import ApiUser

class UserWatchedMovies(models.Model):
    user = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieDetail, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')

class UserWatchlistMovies(models.Model):
    user = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieDetail, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')
