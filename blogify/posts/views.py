from django.shortcuts import render


def index(request):
    template = "posts/index.html"
    title = "Blogify"
    context = {
        "title": title,
    }
    return render(request, template, context)


def group_posts(request):
    template = "posts/group_list.html"
    title = "Blogify - posts"
    context = {
        "title": title,
    }
    return render(request, template, context)
