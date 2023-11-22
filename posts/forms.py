from django import forms
from .models import Post


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