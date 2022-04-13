from django.db import models
from user.models import User
# Create your models here.

class StickyNotes(models.Model):
    textIs = models.TextField(null = False)
    dateOf = models.DateField(null = False)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)




class Categories(models.Model):
    name = models.CharField(max_length=80 ,null = False)
    dateOf = models.DateField(null = False)
    cimg = models.ImageField(upload_to = 'categories/')
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
  