from multiprocessing import context
from django.urls import reverse
from django.views import generic
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # The post instance for this view

        # Retrieve comments and order by date
        comments = post.comment_set.all().order_by('-date')

        context['comments'] = comments
        return context

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
    
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment_date = form.cleaned_data['date']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            date=comment_date,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)