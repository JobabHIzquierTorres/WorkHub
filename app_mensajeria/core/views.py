from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "App de mensajería", "content": "SaaS enfocado a comunicación interna y productividad corporativa "})


class SamplePageView(TemplateView):
    template_name = 'core/sample.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Ejemplo'

        return context
