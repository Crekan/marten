# Generated by Django 4.1.4 on 2022-12-24 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0030_comment_products_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.products'),
        ),
        migrations.AddField(
            model_name='products',
            name='comments',
            field=models.CharField(max_length=150, null=True, verbose_name='Comments'),
        ),
    ]
