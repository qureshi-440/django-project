from django.db import models

# Create your models here.

class Destination(models.Model) :
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200) 
    discrption = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='downloads')