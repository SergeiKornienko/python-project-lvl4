from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'username', 'email',
            'password1', 'password2',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control border'},
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control border'},
            ),
            'username': forms.TextInput(
                attrs={'class': 'form-control border'},
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control border'},
            ),
            'password1': forms.PasswordInput(
                attrs={'class': 'form-control border'},
            ),
            'password2': forms.PasswordInput(
                attrs={'class': 'form-control border'},
            ),
        }
