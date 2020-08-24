from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserWatchedMoviesSerializer, UserWatchlistMoviesSerializer
from movie_scrapper.serializers import MovieDetailSerializer
from .models import UserWatchedMovies, UserWatchlistMovies

class UserWatchListMoviesView(APIView):

    def put(self, request, movie_id):
        data = {}
        data['user'] = request.user.pk
        data['movie'] = movie_id
        serializer = UserWatchlistMoviesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data
            })
        else:
            return Response({
                    'errors': serializer.errors
                }, 201)

    def delete(self, request, movie_id):
        data = {}
        data['movie'] = movie_id
        watchlist_movie = get_object_or_404(UserWatchlistMovies, pk=movie_id)
        watchlist_movie.delete()
        return Response({
                    'message': "successfully deleted 1 object"
                })

class UserWatchListMoviesListView(APIView):

    def get(self, request):
        result = UserWatchlistMovies.objects.filter(
                        user=request.user).prefetch_related('movie')
        result = [item.movie for item in result]
        result = MovieDetailSerializer(result, many=True)
        return Response({
               "data": result.data
            })

class UserWatchedMoviesListView(APIView):

    def get(self, request):
        result = UserWatchlistMovies.objects.filter(
                        user=request.user).prefetch_related('movie')
        result = [item.movie for item in result]
        result = MovieDetailSerializer(result, many=True)
        return Response({
               "data": result.data
            })

class UserWatchedMoviesView(APIView):

    def put(self, request, movie_id):
        data = {}
        data['user'] = request.user.pk
        data['movie'] = movie_id
        serializer = UserWatchedMoviesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data
            })
        else:
            return Response({
                    'errors': serializer.errors
                }, 201)

    def delete(self, request, movie_id):
        data = {}
        watched_movie = get_object_or_404(UserWatchedMovies, pk=movie_id)
        watched_movie.delete()
        return Response({
                    'message': "successfully deleted 1 object"
                })
