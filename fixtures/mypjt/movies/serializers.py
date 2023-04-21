from rest_framework import serializers
from .models import Actor, Movie, Review

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'release_date', 'poster_path')

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview')

class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id','name',)


class ActorDetailSerializer(serializers.ModelSerializer):
    movie_set = MovieTitleSerializer(many =True)
    # movie_title = serializers.CharField(source='movie_set.title')
    class Meta(ActorSerializer.Meta):
        fields = ActorSerializer.Meta.fields +(
            'movie_set',
        )
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     # rep.pop('movie_set', [])
    #     return rep

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)
        

class ActorNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('name',)


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many=True)
    review_set = ReviewSerializer(many=True)

    class Meta(MovieListSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ('actors', 'review_set')

class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta(ReviewSerializer.Meta):
        fields = ('id',) + ReviewSerializer.Meta.fields + (
            'movie',
        )
        read_only_fields = ('movie',)


        