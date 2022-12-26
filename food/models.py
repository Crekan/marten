from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Slider(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='Product Slider', null=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'


class Products(models.Model):
    images = models.FileField(upload_to='products_images/', verbose_name='Image')
    title = models.CharField(max_length=200, verbose_name='Header')
    slug = models.SlugField(unique=True, max_length=250, verbose_name='Url', db_index=True, null=True)
    description = models.TextField(verbose_name='Description', null=True)
    new_price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='New price')
    old_price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, verbose_name='Old price', default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category', null=True,
                                 related_name='product_category')
    availability = models.ForeignKey('Availability', on_delete=models.CASCADE, verbose_name='Availability', null=True)
    vendor_code = models.CharField(max_length=255, verbose_name='Vendor Code', null=True)
    color = models.ManyToManyField('Color', verbose_name='Color')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity', null=True)
    long_description = models.TextField(verbose_name='Full description', null=True)
    # More information
    name = models.CharField(max_length=250, verbose_name='Name', null=True)
    size = models.ManyToManyField('Size')
    length = models.ManyToManyField('Length')
    brand = models.ManyToManyField('Brand')

    # Reviews

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


class ProductsImage(models.Model):
    products = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.products.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='')

    def __str__(self):
        return f'Basket for {self.user.username} | Product {self.product.title}'

    def sum(self):
        return self.product.new_price * self.quantity


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


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name Brand')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def get_absolute_url(self):
        return reverse('brand', kwargs={
            'brand_id': self.id
        })


class Color(models.Model):
    name = models.CharField(max_length=250, verbose_name='Color')

    def __str__(self):
        return self.name


class Availability(models.Model):
    title = models.CharField(max_length=250, verbose_name='Availability')

    def __str__(self):
        return self.title


class Size(models.Model):
    size = models.CharField(max_length=100, verbose_name='Size')

    def __str__(self):
        return self.size


class Length(models.Model):
    length = models.CharField(max_length=100, verbose_name='length')

    def __str__(self):
        return self.length
