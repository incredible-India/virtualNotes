from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=50,null=False,)
    lname = models.CharField(max_length=50,null=False,)
 
    email = models.EmailField(max_length=50,null=False)
  
    password = models.CharField(max_length=50,null=False)
    image = models.ImageField(upload_to='./static/Faculty/img')