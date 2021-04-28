from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    """Form of status."""
    class Meta:
        model = Status
        fields = ('name',)
        widgets = {'name': forms.TextInput(attrs={
            'class': 'form-control border',
            'placeholder': 'Имя',
        })}
