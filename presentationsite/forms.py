from django import forms
from .models import EmailModel

class EmailForm(forms.ModelForm):
    """Form to add a new email."""

    class Meta:
        """Form options."""

        model = EmailModel
        fields = ['email']
