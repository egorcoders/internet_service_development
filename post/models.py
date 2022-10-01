from django.db import models


class Post(models.Model):
    """Таблица постов пользователя."""
    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.TextField(verbose_name='Текст поста')

    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания поста')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата редактирования поста')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Таблица комментариев пользователя."""
    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             related_name="comments",
                             verbose_name='Пост комментария')
    message = models.TextField(verbose_name='Текст комментария')

    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата редактирования комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at',)

    def __str__(self):
        return self.post

