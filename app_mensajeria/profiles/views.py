from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from registration.models import Profile, User

# Create your views here.


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profiles_list.html'
    paginate_by = 3


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
