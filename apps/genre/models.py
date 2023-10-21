from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Name of genre"
    )
    description = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Description of genre"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
