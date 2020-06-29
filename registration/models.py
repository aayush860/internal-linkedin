from django.db import models

# Create your models here.
class Signup(models.Model):
    FullName = models.TextField()
    Email = models.EmailField(max_length=256)
    MobileNumber = models.IntegerField()
    Username = models.CharField(max_length=16)
    Password = models.CharField(max_length=32)

class Signin(models.Model):
    Username = models.CharField(max_length=16)
    Password = models.CharField(max_length=32)

