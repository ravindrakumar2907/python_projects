from pyexpat import model
from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    createTimestamp = models.DateTimeField(auto_now=True)