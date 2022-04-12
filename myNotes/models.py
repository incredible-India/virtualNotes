from django.db import models
from user.models import User
# Create your models here.

class StickyNotes(models.Model):
    textIs = models.TextField(null = False)
    dateOf = models.DateField(null = False)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)