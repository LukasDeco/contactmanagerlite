from django import forms

from .models import Contact

class NewContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone_number', 'email_address')
