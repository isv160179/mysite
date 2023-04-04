from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),)
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique_for_date='publish',
                            verbose_name='Строка идентификатор')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts',
                               verbose_name='Автор блога')
    body = models.TextField(verbose_name='Текст блога')
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name='Время публикации')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Время изменения')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft',
                              verbose_name='Статус блога')


class Meta:
    ordering = ('-publish',)
    verbose_name = "Блог"
    verbose_name_plural = "Блоги"


def __str__(self):
    return self.title
