# Generated by Django 4.1.4 on 2022-12-24 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0042_rename_product_name_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='eating',
        ),
    ]
