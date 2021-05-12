from django.db import models

# Create your models here.

class chalan(models.Model):
    names = models.CharField(max_length = 200)
    phonenumber = models.CharField(max_length = 200)
    place = models.CharField(max_length = 200)
    licensenumber = models.CharField(max_length = 200)
    vehiclenumber = models.CharField(max_length = 200)
    vehicletype = models.CharField(max_length = 200)
    creator = models.CharField(max_length = 200)