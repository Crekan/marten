# Generated by Django 4.1.4 on 2022-12-23 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0027_remove_products_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Length',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.CharField(max_length=100, verbose_name='length')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100, verbose_name='Size')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.ManyToManyField(to='food.brand'),
        ),
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.ManyToManyField(to='food.color', verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='products',
            name='length',
            field=models.ManyToManyField(to='food.length'),
        ),
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.ManyToManyField(to='food.size'),
        ),
    ]