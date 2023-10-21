from rest_framework import serializers

from .models import Book, Bookmark
from apps.genre.serializers import GenreSerializer
from apps.author.serializers import AuthorSerializer
from apps.review.serializers import ReviewSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'authors': {'required': False},
            'genres': {'required': False},
        }


class BookmarkForBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id',)


class BookmarkSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'book')


class BookRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    authors = AuthorSerializer(many=True)
    book_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    authors = AuthorSerializer(many=True)
    book_bookmarks = BookmarkForBookListSerializer(many=True)

    class Meta:
        model = Book
        fields = ("title", "genres", "authors", "average_rating", "book_bookmarks")
