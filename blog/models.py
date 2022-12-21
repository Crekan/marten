from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/', verbose_name='Image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    date_added = models.DateField(auto_now=True, verbose_name='Date Added')
    title = models.CharField(max_length=250 ,verbose_name='Header')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
