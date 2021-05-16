from django.db import models


# Create your models here.

class challan(models.Model):

    names = models.CharField(max_length = 200)
    phonenumber = models.IntegerField()
    place = models.CharField(max_length = 200)
    licensenumber = models.CharField(max_length = 200)
    vehiclenumber = models.CharField(max_length = 200)
    vehicletype = models.CharField(max_length=200, default=None, blank=True, null=True)
    creator = models.CharField(max_length = 200)

    def __str__(self):
        return self.licensenumber


class dynamicAbout(models.Model):

    title = models.CharField(max_length = 200)
    desc = models.TextField()

    def __str__(self):
        return self.title


class contact(models.Model):

    usernames = models.CharField(max_length = 200)
    phonenumbers = models.IntegerField()
    email = models.EmailField(max_length = 200)
    descs = models.TextField()

    def __str__(self):
        return self.email

class HomeImage(models.Model):
    caption = models.CharField(max_length=50)
    image = models.FileField(upload_to='picture', blank = True)

    def str(self):
      return self.caption