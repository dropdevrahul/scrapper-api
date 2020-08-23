from django.db import models
from user_app.models import ApiUser

class MovieDetail(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=500)
    storyline = models.TextField()
