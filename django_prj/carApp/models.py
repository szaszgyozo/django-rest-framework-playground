
from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

class CarOwner(models.Model):
    user = models.ForeignKey(
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

    owner = models.OneToOneField(
        CarOwner,
        on_delete=models.RESTRICT,
        default=None,
        null=False,
        blank=False
    )


