from django.urls import path
from .views import CalendarView, EventsJsonView, EventCreateJsonView, EventCreateView

userCalendar_patterns = ([
    path('', CalendarView.as_view(), name='calendar_view'),
    path("events/", EventsJsonView.as_view(), name="events_json"),
    path("event/add/", EventCreateView.as_view(), name="event_add"),
    path("event/add-json/", EventCreateJsonView.as_view(), name="event_add_json"),
]), 'calendar'
