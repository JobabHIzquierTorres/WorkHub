from django.db import models
from registration.models import Profile
from django.contrib.auth.models import User

# Create your models here.


class UserCalendar(models.Model):
    user = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name='Calendario')
    title = models.CharField(max_length=50, verbose_name='Título')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado el')

    def __str__(self) -> str:
        return f'Calendario de {self.user.user.username}'


class CalendarEvent(models.Model):
    userCalendar = models.ForeignKey(
        UserCalendar, on_delete=models.CASCADE, related_name='Eventos')
    title = models.CharField(max_length=100, verbose_name='Título del evento')
    description = models.TextField(
        blank=True, null=True, verbose_name='Descripción')
    start_date = models.DateTimeField(verbose_name='Fecha de inicio')
    end_date = models.DateTimeField(
        verbose_name='Fecha de fin', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        return f"{self.title} ({self.start_date.date()})"
