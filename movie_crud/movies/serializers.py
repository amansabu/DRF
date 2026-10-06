from typing import Any

from rest_framework import serializers


from movies.models import Movie
class MovieSerializer(serializers.Serializer):
    title=serializers.CharField()
    director=serializers.CharField()
    language=serializers.CharField()
    year=serializers.CharField()
    rating=serializers.FloatField()
    runtime=serializers.IntegerField()


    #After validation and before saving
    def create(self, validated_data):

        m=Movie.objects.create(**validated_data)
        return m