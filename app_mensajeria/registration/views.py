from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms

from .forms import UserCreationFormEmail, Profileform, EmailFormUpdate
from .models import Profile


# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationFormEmail
    template_name = 'registration/signup.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super().get_form()

        # runtime widgets modifications
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repita la Contraseña'})

        # labels = None
        for item in form.fields.values():
            item.label = ''

        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = Profileform

    success_url = reverse_lazy('registration:profile')
    template_name = 'registration/profile_form.html'

    # get or create user profile
    def get_object(self) -> Model:
        profile, created = Profile.objects.get_or_create(
            user=self.request.user)

        return profile

    # labels = None
    def get_form(self, form_class=None):
        form = super().get_form()

        for labels in form.fields.values():
            labels.label = ''

        return form


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailFormUpdate

    success_url = reverse_lazy('registration:profile')
    template_name = 'registration/profile_email_form.html'

    # obtain the user instance we want to edit
    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form()

        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})

        return form
