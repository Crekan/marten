# Generated by Django 4.1.4 on 2023-01-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True, verbose_name='Url'),
        ),
    ]
