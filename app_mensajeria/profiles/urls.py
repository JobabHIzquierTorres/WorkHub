from django.urls import path
from .views import ProfileListView, ProfileDetailView

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='profiles_list'),
    path('<username>/', ProfileDetailView.as_view(), name='profile_detail')

]), 'profiles'
