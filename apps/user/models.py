import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    activate_token = models.UUIDField(
        null=True,
        blank=True,
        verbose_name="Activation token for account"
    )

    def save(self, *args, **kwargs):
        if not self.activate_token:
            self.activate_token = uuid.uuid4()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
