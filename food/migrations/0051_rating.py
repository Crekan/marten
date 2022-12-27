# Generated by Django 4.1.4 on 2022-12-25 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0050_ratingstar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=18, verbose_name='IP address')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.products', verbose_name='Product')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.ratingstar', verbose_name='Stat')),
            ],
        ),
    ]