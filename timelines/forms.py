from django import forms
from .models import Post, Comment

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text','image')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('text',)