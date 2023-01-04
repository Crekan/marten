from django.db import models
from tinymce.models import HTMLField


class Cards(models.Model):
    images = models.ImageField(upload_to='cards_images/', verbose_name='Images')
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    advantages = HTMLField(verbose_name='Advantages')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class Statistics(models.Model):
    years_in_business = models.PositiveIntegerField()
    happy_people = models.PositiveIntegerField()
    billion_sales = models.PositiveIntegerField()
    award_winning = models.PositiveIntegerField()

    def __str__(self):
        return f'main statistics – {self.id}'

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'


class Team(models.Model):
    images = models.ImageField(upload_to='team_images/', verbose_name='Images')
    fio = models.CharField(max_length=255, verbose_name='FIO')
    job_title = models.CharField(max_length=250, verbose_name='Job Title')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
