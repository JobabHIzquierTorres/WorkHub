from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


# extends form to add email validation


class UserCreationFormEmail(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Introduzca un email válido.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # It has its own validations; replacing the widget will override them. Modify it at runtime instead.

    # email validator
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email ya en uso")
        return email


class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'name', 'jobPosition')

        # widgets modifications
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control-file mt-3'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Nombre Completo'
            }),
            'jobPosition': forms.TextInput(attrs={
                'class': 'form-control mt-3', 'placeholder': 'Puesto de trabajo actual'
            })
        }


class EmailFormUpdate(forms.ModelForm):
    email = forms.EmailField(
        required=True, help_text="Introduzca un email válido.")

    class Meta:
        model = User
        fields = ('email',)

    # email validator
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email ya en uso')
        return email
