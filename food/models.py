from django.db import models


class Slider(models.Model):
    images = models.ImageField(upload_to='slider_images/', verbose_name='Image')
    description = models.CharField(max_length=150, verbose_name='Description')
    title = models.CharField(max_length=250, verbose_name='Header')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'


class Products(models.Model):
    images = models.ImageField(upload_to='products_images/', verbose_name='Image')
    title = models.CharField(max_length=200, verbose_name='Header')
    description = models.TextField(verbose_name='Description', null=True)
    new_price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='New price')
    old_price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, verbose_name='Old price', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


class BestProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Best Product')
    end_of_discount = models.DateField(null=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Best Product'
        verbose_name_plural = 'Best Products'


class CommentsHome(models.Model):
    comment = models.TextField(verbose_name='Comment')
    images = models.ImageField(upload_to='comments_home_images/', verbose_name='Photo')
    full_name = models.CharField(max_length=255, verbose_name='Full name')
    profession = models.CharField(max_length=150, verbose_name='Profession')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Comment Home'
        verbose_name_plural = 'Comment Home'
