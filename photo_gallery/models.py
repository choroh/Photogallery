from django.db import models
from django.urls import reverse


class Category(models.Model):
    cat_title = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/categories/", verbose_name='Картинка категории')

    def __str__(self):
        return self.cat_title

    def get_absolute_url(self):
        # Для выбора категорий
        return reverse('cat', kwargs={'cat_id': self.pk})
        # return reverse('cat', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['cat_title']


class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото")
    ico = models.ImageField(upload_to="photos/ico/", verbose_name='Иконка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat_title = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Для выбора категорий
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалереи'
        ordering = ['time_create', 'title']
