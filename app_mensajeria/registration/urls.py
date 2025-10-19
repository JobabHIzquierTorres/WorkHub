from .views import SignUpView, ProfileUpdate, EmailUpdate
from django.urls import path

registration_patterns = ([
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdate.as_view(), name='email_update'),
]), 'registration'
