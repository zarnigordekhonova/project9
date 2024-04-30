from django.db import models

# Create your models here.
class Cars(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=255)



    def __str__(self):
        return f'{self.model} {self.make}'



class Vehicles(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    type = models.CharField(max_length=255)



    def __str__(self):
        return f'{self.model} {self.make}'

