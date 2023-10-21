from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Last Name"
    )
    patronymic = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Patronymic"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}".strip()

    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        if self.patronymic:
            full_name = f"{self.last_name} {self.first_name} {self.patronymic}"
        return full_name.strip()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
