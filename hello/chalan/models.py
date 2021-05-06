from django.db import models

# Create your models here.

class challan(models.Model):
    names = models.CharField(max_length = 200)
    phonenumber = models.IntegerField(max_length = 200)
    place = models.CharField(max_length = 200)
    licensenumber = models.IntegerField(max_length = 200)
    vehiclenumber = models.CharField(max_length = 200)
    vehicletype = models.CharField(max_length = 200)
    creator = models.CharField(max_length = 200)

    def __str__(self):
        return self.licensenumber