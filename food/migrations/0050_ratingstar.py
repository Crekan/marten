# Generated by Django 4.1.4 on 2022-12-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0049_rename_products_basket_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Value')),
            ],
        ),
    ]
