from django.contrib.auth.models import User
from django.db import models

#  function one profile image by user


def custom_upload_to(instance, filename):
    first_instance = Profile.objects.get(pk=instance.pk)
    first_instance.avatar.delete()

    return 'profiles/' + filename


# Create your models here.


class Profile(models.Model):
    # relation with model User
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(
        upload_to=custom_upload_to,
        null=True,
        blank=True)
    name = models.CharField(
        max_length=150,
        verbose_name='Nombre Completo')
    jobPosition = models.CharField(
        null=True,
        blank=True)

    class Meta:
        ordering = ['name']
