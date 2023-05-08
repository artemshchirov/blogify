from django.http import HttpResponse


def index(request):
    return HttpResponse('Добро пожаловать на Главную страницу!')


def group_posts(request, slug):
    return HttpResponse(f'Добро пожаловать на страницу group/{slug}!')
