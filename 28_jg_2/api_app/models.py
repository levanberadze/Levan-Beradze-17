from django.db import models
from datetime import datetime
from django.utils import timezone


class Person(models.Model):
    GENDER_CHOICES = {'m': 'Male',
                      'f': 'Female'}
    name = models.CharField(max_length=250)
    race = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             related_name='person')
    create_date = models.DateTimeField(default=timezone.now)
    birth_date = models.DateTimeField()

    @property
    def age(self):
        return (datetime.today() - self.birth_date.replace(tzinfo=None)).days // 365


class City(models.Model):
    zip = models.CharField(max_length=4)
    name = models.CharField(max_length=168)

    def __str__(self):
        return f'{self.zip}-{self.name}'

