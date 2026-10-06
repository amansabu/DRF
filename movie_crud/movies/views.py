from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


from movies.serializers import MovieSerializer


# Create your views here.
# //GET,POST,PUT,PATCH,Delete

#API View for reading all movie records

#queryset
#serializer object
#Resoinse
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.response import Response
class MovieList(APIView):
    def get(self,request):

        #qs
        m=Movie.objects.all()

        #serializer instance
        serializer_instance=MovieSerializer(m,many=True)

        #Response
        return Response(serializer_instance.data)


#API View for creating a nwe record

class MovieCreate(APIView):
    def post(self,request):
        form_data=request.data
        serializers_instance=MovieSerializer(data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data)
        else:
            return Response(serializers_instance.errors)
#API View for reading a specific record

#API View for updating a specific record

#API View for deleting a specific record