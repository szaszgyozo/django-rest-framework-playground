from django.db import models
from django.db.models import fields
from django.db.models.enums import Choices
from django.db.models.fields import CharField

# Create your models here.

class UserStatus(models.IntegerChoices):
    ACTIVE = 1,
    INACTIVE = 0

class UserProfile(models.Model):
    id = models.CharField(
        max_length=13,
        primary_key=True, 
        editable=False
    )

    phone_nr = models.CharField(
        max_length=13, 
        blank=True
    )

    age = models.IntegerField(
        blank=True
    )

    status = models.IntegerField(
        choices=UserStatus.choices,
        default=UserStatus.ACTIVE
    )