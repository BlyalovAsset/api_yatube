from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import LENGTH_TEXT, max_length

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    text = models.TextField(verbose_name='Запись')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        db_index=True
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Сообщество'
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Group(models.Model):
    title = models.CharField(
        max_length,
        verbose_name='Название сообщества',
        db_index=True
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='адрес'
    )
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации',
        db_index=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='запись'
    )

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created',)

    def __str__(self):
        return self.text[:LENGTH_TEXT]
