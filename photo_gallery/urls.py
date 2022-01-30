from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('login/', login, name='login'),
    path('cat/<int:cat_id>', show_category, name='cat'), # Вместо цифровой адресации сделаем по slug
    #path('cat/<slug:cat_slug>/', show_category, name='cat'),
    path('post/<int:post_id>', show_post, name='post'),
]


