from django import forms
from .models import Post, PostImage
from django.forms import modelformset_factory


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'content', 'status', 'image']
        exclude = ['author', 'slug']

PostImageFormSet = modelformset_factory(
    PostImage,
    fields=('image',),
    extra=0,
    can_delete=True
)