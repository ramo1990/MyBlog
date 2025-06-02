from django import forms
from django.contrib.auth.models import User
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {'message':forms.Textarea(attrs={'rows':4}),}


# class AProposForm(forms.ModelForm):
#     class Meta:
#         model = APropos
#         fields = ['title', 'content', 'image']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
#             'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
#         }