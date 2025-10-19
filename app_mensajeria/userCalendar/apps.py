from django.apps import AppConfig


class UsercalendarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userCalendar'

    def ready(self):
        import userCalendar.signals
