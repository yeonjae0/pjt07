from rest_framework import serializers
from .models import Actor, Movie, Review

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id','name',)


class ActorDetailSerializer(serializers.ModelSerializer):
    movie_set = MovieSerializer(many =True)
    # movie_title = serializers.CharField(source='movie_set.title')
    class Meta(ActorSerializer.Meta):
        fields = ActorSerializer.Meta.fields +(
            'movie_set',
            'movie_title',
        )




class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)
        