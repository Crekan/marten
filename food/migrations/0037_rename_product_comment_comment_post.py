# Generated by Django 4.1.4 on 2022-12-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0036_rename_products_comment_product_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product_comment',
            new_name='post',
        ),
    ]
