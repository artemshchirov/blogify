from django.shortcuts import render, get_object_or_404

from . models import Post, Group


def index(request):
    template = 'posts/index.html'
    title = 'Blogify'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
        'text': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group.html'
    posts = group.posts.all()
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
