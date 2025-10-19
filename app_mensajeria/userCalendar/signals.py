from django.db.models.signals import post_save
from django.dispatch import receiver
from registration.models import Profile
from .models import UserCalendar


@receiver(post_save, sender=Profile)
def create_user_calendar(sender, instance, created, **kwargs):
    if created:
        UserCalendar.objects.get_or_create(
            user=instance, title="Mi calendario")
