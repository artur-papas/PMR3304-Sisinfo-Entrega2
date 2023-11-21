from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post

def list_posts(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)

def detail_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def create_post(request):
    if request.method == 'POST':
        post_title = request.POST['title']
        post_publish_date = request.POST['publish_date']
        post_content = request.POST['content']
        post = Post(title=post_title,
                      publish_date=post_publish_date,
                      content=post_content)
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})


# Create your views here.
