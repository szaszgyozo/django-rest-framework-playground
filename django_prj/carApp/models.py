
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class CarOwner(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=CASCADE,
        blank=False,
        null=False
    )

class Car(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False
    )

    horse_power = models.IntegerField(
        blank=False
    )

    owner = models.ForeignKey(
        CarOwner,
        on_delete=models.CASCADE,
        related_name='cars',
        default=None,
        null=False,
        blank=False
    )
