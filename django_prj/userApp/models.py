from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):

    class UserStatus(models.IntegerChoices):
        ACTIVE = 1,
        INACTIVE = 0

    phone_nr = models.CharField(
        max_length=13, 
        blank=True
    )

    age = models.IntegerField(
        blank=True,
        null=True
    )

    status = models.IntegerField(
        choices=UserStatus.choices,
        default=UserStatus.ACTIVE
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=False,
        blank=False
    )



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
