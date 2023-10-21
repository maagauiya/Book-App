from rest_framework import serializers

from .models import Book, Bookmark
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


class BookListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ("title", "genres", "authors", "average_rating")


class BookRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookmarkSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'book')
