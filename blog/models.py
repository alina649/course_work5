from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображеие', **NULLABLE)
    creation_date = models.TimeField(verbose_name='дата создания', auto_now_add=True)

    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    sign_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "статьи"
