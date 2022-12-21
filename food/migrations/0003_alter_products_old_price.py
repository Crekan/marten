# Generated by Django 4.1.4 on 2022-12-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_products_alter_slider_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, verbose_name='Old price'),
        ),
    ]
