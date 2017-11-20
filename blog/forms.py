from django import forms
from .models import Post, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')   # why is this not in the model file? Does migrate create the blog from this?

        
class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'content') 