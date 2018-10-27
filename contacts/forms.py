from django import forms
from .models import Contact

__all__ = (
    'ContactModelForm',
)


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name',)
