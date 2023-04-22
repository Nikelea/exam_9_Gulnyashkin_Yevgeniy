from django.db import models
from django.contrib.auth import get_user_model


class Publication(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False, blank=False, related_name='publications')
    image = models.ImageField(blank=False, upload_to='images', verbose_name='Публикация')
    description = models.TextField(max_length=2000, blank=False, verbose_name='Описание')
    likes_counter = models.IntegerField(null=True, blank=False, default=0, verbose_name='Число лайков')
    comments_counter = models.IntegerField(null=True, blank=False, default=0, verbose_name='Число комментариев')
    likes = models.ManyToManyField(get_user_model(), related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Comments(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='publications.Publication', related_name='comments', null=False,
                             blank=False, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Описание', null=False, blank=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
