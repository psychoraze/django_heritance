from django import forms
from .models import Pet, Post


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'pic', 'story']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'description', 'image', 'posted_by']

