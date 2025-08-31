from django.db import models

# Create your models here.
class Malware(models.Model):
     
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)

class contactus(models.Model):
    firstname=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    mobile=models.IntegerField()
    message=models.CharField(max_length=400)