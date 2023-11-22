from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

def list_posts(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            post_publish_date = form.cleaned_data['publish_date']
            post_content = form.cleaned_data['content']
            post = Post(title=post_title,
                        publish_date=post_publish_date,
                        content=post_content)
            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))
    else:
        form=PostForm
    context={'form': form}
    return render(request, 'posts/create.html', context)

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.publish_date = form.cleaned_data['publish_date']
            post.content = form.cleaned_data['content']
            post.save()
            return HttpResponseRedirect(reverse('posts:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={'title': post.title,
                'publish_date': post.publish_date,
                'content': post.content
            })
    context = {'post': post, 'form': form}
    return render(request, 'posts/update.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)
# Create your views here.
