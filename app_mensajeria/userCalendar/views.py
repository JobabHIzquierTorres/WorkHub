from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.utils.dateparse import parse_datetime

from .models import CalendarEvent
from registration.models import Profile

import json

# Create your views here.


class CalendarView(LoginRequiredMixin, TemplateView):
    template_name = "userCalendar/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the user authenticated profile
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context


class EventsJsonView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_calendar = request.user.profile.Calendario
        eventos = user_calendar.Eventos.all()

        data = [
            {
                "title": evento.title,
                "start": evento.start_date.isoformat(),
                "end": evento.end_date.isoformat() if evento.end_date else None,
            }
            for evento in eventos
        ]
        return JsonResponse(data, safe=False)


class EventCreateView(LoginRequiredMixin, CreateView):
    model = CalendarEvent
    fields = ["title", "description", "start_date", "end_date"]
    template_name = "userCalendar/event_form.html"
    success_url = reverse_lazy("calendar_view")

    def form_valid(self, form):
        form.instance.userCalendar = self.request.user.profile.Calendario   # type: ignore
        return super().form_valid(form)


class EventCreateJsonView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):

        data = json.loads(request.body)
        title = data.get("title")
        start_date = parse_datetime(data.get("start"))
        end_raw = data.get("end")
        end_date = parse_datetime(end_raw) if end_raw else None

        user_calendar = request.user.profile.Calendario  # type: ignore

        evento = CalendarEvent.objects.create(
            userCalendar=user_calendar,
            title=title,
            start_date=start_date,
            end_date=end_date
        )

        return JsonResponse({
            "id": evento.id,  # type:ignore
            "title": evento.title,
            "start": evento.start_date.isoformat(),
            "end": evento.end_date.isoformat() if evento.end_date else None,
        })
