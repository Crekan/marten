# Generated by Django 4.1.4 on 2022-12-23 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0028_length_size_products_brand_products_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='images',
            field=models.FileField(upload_to='products_images/', verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/')),
                ('products', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='food.products')),
            ],
        ),
    ]
