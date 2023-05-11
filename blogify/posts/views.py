from django.shortcuts import render

from . models import Post


def index(request):
    template = 'posts/index.html'
    title = 'Blogify'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_list.html'
    title = 'Blogify - posts'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)
