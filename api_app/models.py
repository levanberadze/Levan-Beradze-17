from django.db import models
from datetime import datetime, tzinfo


class Person(models.Model):
    GENDER_CHOICES = {'m': 'Male',
                      'f': 'Female'}
    name = models.CharField(max_length=250)
    age = models.IntegerField(default=18)
    race = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    city = models.OneToOneField('City', on_delete=models.CASCADE,
                                    related_name='person')
    create_date = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateTimeField()


    @property
    def age(self):
        return (datetime.today() - self.birth_date.replace(tzinfo=None)).days // 365


class City(models.Model):
    zip = models.CharField(max_length=4)
    create_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=168)

    def __str__(self): return f'{self.zip}-{self.name}'