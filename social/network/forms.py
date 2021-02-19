from .models import Post
from django import forms


class PostForm(forms.ModelForm):
  '''create form for Post'''
  class Meta:
    model = Post
    fields = ['body']
    labels = {'body': 'New Post'}
    widgets = {'body': forms.TextInput(attrs = {'class': 'form-control'})}
