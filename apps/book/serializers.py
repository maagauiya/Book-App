from rest_framework import serializers

from .models import Book
from apps.genre.serializers import GenreSerializer
from apps.author.serializers import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'authors': {'required': False},
            'genres': {'required': False},
        }


class BookGetRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
