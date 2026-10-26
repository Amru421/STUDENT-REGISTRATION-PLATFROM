from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('topic', 'languages_used', 'duration')
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'languages_used': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }