from django.contrib import admin

# Register your models here.
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_title', 'photo')
    list_display_links = ('id', 'cat_title')
    search_fields = ('cat_title',)
    #prepopulated_fields = {"slug": ("cat_title",)}  # автоматически заполнять слаг на основе названия


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'photo', 'ico', 'time_create', 'is_published', 'cat_title')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description')
    #prepopulated_fields = {"slug": ("title",)}  # автоматически заполнять слаг на основе названия


admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
