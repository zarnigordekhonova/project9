from django.db import models

# Create your models here.

class Personal_info1(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.name} {self.surname}'


class Personal_info2(models.Model):
    workplace = models.CharField(max_length=255)
    salary = models.IntegerField()
    since_when = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.workplace} {self.salary}'

