from rest_framework import serializers
from .models import MovieDetail


class ScrapperRequestSerializer(serializers.Serializer):
    movie_list_url = serializers.URLField()

class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieDetail
        fields = '__all__'
