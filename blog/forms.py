from django import forms

from .models import Post

class PubForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)