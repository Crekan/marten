# Generated by Django 4.1.4 on 2022-12-27 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0054_rename_rating_rating_rate_alter_rating_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
