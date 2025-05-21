from django import forms
from django.contrib.auth.models import User
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {'message':forms.Textarea(attrs={'rows':4}),}
