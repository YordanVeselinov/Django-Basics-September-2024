from django.core.validators import MinLengthValidator
from django.db import models
from MyMusicApp.profiles.validators import NumericAlphaValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            NumericAlphaValidator(),
            MinLengthValidator(3)
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
