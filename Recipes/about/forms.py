from django import forms

from .models import HelpFormModel


class HelpForm(forms.ModelForm):
    class Meta:
        model = HelpFormModel
        fields = ('name', 'text', 'email',)
