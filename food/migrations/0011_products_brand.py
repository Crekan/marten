# Generated by Django 4.1.4 on 2022-12-21 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.brand', verbose_name='Brand'),
        ),
    ]
