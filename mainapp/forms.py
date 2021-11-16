from django.forms import ModelForm
from .models import Post


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