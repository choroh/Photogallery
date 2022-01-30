
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Категории", 'url_name': 'home'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'cats': posts,  # публикуем список категорий
        'title': 'Фотогалерея',
        'cat_selected': 0,
        'class': "img-full"
    }
    #print('posts', posts)
    return render(request, 'photo_gallery/index.html', context=context)


def show_category(request, cat_id):
    posts = Gallery.objects.filter(cat_title=cat_id)
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Фотографии по категориям',
        'cat_selected': cat_id,
        'class': "img-ico"
    }
    return render(request, 'photo_gallery/index.html', context=context)


def show_post(request, post_id):
    post = get_object_or_404(Gallery, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post_id,
        'class': "img-full"
    }

    return render(request, 'photo_gallery/photo.html', context=context)


def login(request):
    return HttpResponse('Войти')


def about(request):
    return render(request, 'photo_gallery/about.html', {'menu': menu, 'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1')
