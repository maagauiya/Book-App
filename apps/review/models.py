from django.db import models

from apps.book.models import Book
from apps.user.models import User


class Review(models.Model):
    text = models.TextField(
        verbose_name="Review Text",
        null=True,
        blank=True,
    )
    rating = models.FloatField(
        verbose_name="Rating"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_reviews',
        verbose_name="Book",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_reviews',
        verbose_name="User",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.user} - {self.book}"
