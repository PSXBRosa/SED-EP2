from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'content',
        ]
        labels = {
            'title': 'Título',
            'slug': 'Endereço',
            'content': 'Conteúdo',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'content',
        ]
        labels = {
            'author' : 'Autor',
            'content': 'Conteúdo',
        }