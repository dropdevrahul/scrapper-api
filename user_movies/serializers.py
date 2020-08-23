from rest_framework import serializers
from .models import UserWatchedMovies, UserWatchlistMovies

class UserWatchedMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWatchedMovies
        fields = '__all__'

class UserWatchlistMoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserWatchlistMovies
        fields = '__all__'
