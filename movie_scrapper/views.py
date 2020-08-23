from rest_framework.response import Response
from rest_framework.views import APIView
from .lib import scrap_and_store_movies_details
from .models import MovieDetail
from .serializers import ScrapperRequestSerializer, MovieDetailSerializer


class ScrapperView(APIView):

    def put(self, request):  # use put cuz this operation is idempotent
        request_serializer = ScrapperRequestSerializer(data=request.data)
        if request_serializer.is_valid():
            number_of_movies = scrap_and_store_movies_details(request_serializer.validated_data['movie_list_url'], request.user)
            return Response({'message': "Succesfully scrapped {} movies".format(number_of_movies)})
        else:
            return Response({'errors': request_serializer.errors}, 400)


class MoviesView(APIView):

    def get(self, request):
        result = MovieDetail.objects.all()
        result = MovieDetailSerializer(result, many=True)
        return Response({
            'data': {
                    "movies": result.data
                }
            })
