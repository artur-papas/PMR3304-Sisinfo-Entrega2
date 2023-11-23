from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'publish_date',
            'content',
        ]
        labels = {
            'title': 'Título',
            'publish_date': 'Data de Publicação',
            'content': 'Conteúdo do post',
        }

        widgets = {'publish_date': forms.DateInput(attrs={'type': 'date'})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
            'date',
            'post',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
            'date' : 'Data do comentário',
            'post': 'Post Associado',
        }
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}