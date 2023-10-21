from django.db import models

from apps.author.models import Author
from apps.genre.models import Genre


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
        verbose_name="Genre"
    )
    authors = models.ManyToManyField(
        Author,
        related_name="author_books",
        verbose_name="Author"
    )
    average_rating = models.FloatField(
        default=0,
        verbose_name="Средний рейтинг"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
