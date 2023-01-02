from django.contrib.auth.models import User
from django.db import models

from tinymce.models import HTMLField


class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/', verbose_name='Image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    date_added = models.DateField(auto_now=True, verbose_name='Date Added')
    title = models.CharField(max_length=250, verbose_name='Header')
    slug = models.SlugField(unique=True, max_length=250, verbose_name='Url', db_index=True, null=True)
    description = HTMLField(verbose_name='Description', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.blog.title
