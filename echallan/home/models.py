from django.db import models

# Create your models here.
class Challan(models.Model):

    chalan_amount = models.IntegerField()
    chalan_on_name = models.CharField(max_length = 100)
    creator_officer = models.CharField(max_length = 100)
