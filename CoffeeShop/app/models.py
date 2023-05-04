from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50, blank=True)
    email=models.EmailField(blank=True)
    phone=models.IntegerField(blank=True)
    desc=models.TextField(blank=True)
    

class Review(models.Model):
    name= models.CharField(max_length=50, blank=True)
    desc=models.TextField(blank=True)
