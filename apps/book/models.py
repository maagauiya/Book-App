from django.db import models

from apps.author.models import Author
from apps.genre.models import Genre
from apps.user.models import User


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Title of the book"
    )
    description = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Description of the book"
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="genre_books",
        verbose_name="Genre",
    )
    authors = models.ManyToManyField(
        Author,
        related_name="author_books",
        verbose_name="Author"
    )
    average_rating = models.FloatField(
        default=0,
        verbose_name="Average rating"
    )
    published_date = models.DateTimeField(
        verbose_name="Date of publish",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def recalculate_average_rating(self):
        reviews = self.book_reviews.all()
        total_rating = sum([review.rating for review in reviews])
        self.average_rating = total_rating / reviews.count() if reviews.count() > 0 else 0
        self.save()


class Bookmark(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="user_bookmarks"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Book",
        related_name="book_bookmarks"
    )

    class Meta:
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
