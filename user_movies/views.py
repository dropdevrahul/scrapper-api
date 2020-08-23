from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserWatchedMoviesSerializer, UserWatchlistMoviesSerializer
from .models import UserWatchedMovies, UserWatchlistMovies

class UserWatchListMoviesView(APIView):

    def get(self, request):
        result = UserWatchlistMovies.objects.filter(user=request.user)
        result = UserWatchlistMoviesSerializer(result, many=True)
        return Response({
            "data": result.data
            })

    def put(self, request):
        data = request.data
        data['user'] = request.user.pk
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

class UserWatchedMoviesView(APIView):

    def get(self, request):
        result = UserWatchedMovies.objects.filter(user=request.user)
        result = UserWatchedMoviesSerializer(result, many=True)
        return Response({
            "data": result.data
            })

    def put(self, request):
        data = request.data
        data['user'] = request.user.pk
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
