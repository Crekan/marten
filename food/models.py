from django.db import models


class Slider(models.Model):
    images = models.ImageField(upload_to='slider_images/', verbose_name='Изображение')
    description = models.CharField(max_length=150, verbose_name='Описание')
    title = models.CharField(max_length=250, verbose_name='Заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'
