from django import forms
from .models import Notice

# Modelo de formulario


class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden'}),
        }
        labels = {
            'title': '',
            'content': '',
            'order': ''
        }
