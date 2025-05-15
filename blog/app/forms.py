# from django import forms
# from .models import Post, PostImage
# from django.forms import modelformset_factory


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         # fields = ['title', 'content', 'status', 'image']
#         exclude = ['author', 'slug']

# PostImageFormSet = modelformset_factory(
#     PostImage,
#     fields=('image',),
#     extra=0,
#     can_delete=True
# )

from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('Les mots de passe ne correspondent pas.')

        return cleaned_data
