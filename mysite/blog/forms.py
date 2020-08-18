from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', "title", 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'loader editable medium-editor-textarea posttitle'}),
            'text': forms.Textarea(attrs={'class': 'loader editable medium-editor-textarea postcontent', 'row': '8'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'loader editable medium-editor-textarea authorinputclass'}),
            'text': forms.Textarea(attrs={'class': 'loader editable medium-editor-textarea commentcontent', 'row': '4'}),
        }
