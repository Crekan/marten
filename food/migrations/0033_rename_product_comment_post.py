# Generated by Django 4.1.4 on 2022-12-24 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0032_rename_post_comment_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product',
            new_name='post',
        ),
    ]
