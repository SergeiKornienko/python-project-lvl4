from django import forms
from task_manager.tasks import models


class StatusForm(forms.ModelForm):
    """Form of status."""
    class Meta:
        model = models.Status
        fields = ('name',)
        widgets = {'name': forms.TextInput(attrs={
            'class': 'form-control border',
            'placeholder': 'Имя',
        })}


class TaskForm(forms.ModelForm):
    """Form of status."""
    class Meta:
        model = models.Task
        fields = ('name', 'description', 'status', 'performer',)
        widgets = {'name': forms.TextInput(attrs={
            'class': 'form-control border',
            'placeholder': 'Имя',
        })}
