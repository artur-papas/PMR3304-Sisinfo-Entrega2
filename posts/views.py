from multiprocessing import context
from django.urls import reverse
from django.views import generic
from .models import Post
from .forms import PostForm

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse('posts:detail', args=(self.object.id, ))
    
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'posts/update.html'
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse('posts:detail', args=(self.object.id, ))

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'

    def get_success_url(self) -> str:
        return reverse('posts:index')
