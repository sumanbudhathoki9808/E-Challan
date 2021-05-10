from django.db import models

# Create your models here.

class challan(models.Model):
    Choices = (
        ('Car', 'Car'),
        ('Motercycle', 'Motercycle'),
        ('Bus', 'Bus'),
        ('Van', 'Van'),
        ('Truck', 'Truck'),
    )

    names = models.CharField(max_length = 200)
    phonenumber = models.IntegerField(max_length = 200)
    place = models.CharField(max_length = 200)
    licensenumber = models.CharField(max_length = 200)
    vehiclenumber = models.CharField(max_length = 200)
    vehicletype = models.CharField(max_length=200, null = True, choices= Choices)
    creator = models.CharField(max_length = 200)

    def __str__(self):
        return self.licensenumber