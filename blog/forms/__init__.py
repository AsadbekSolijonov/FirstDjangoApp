from django.forms.models import ModelForm

from blog.models.blog import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
