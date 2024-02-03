from django.db import models

# Create your models here.
class RegisterForm(models.Model):
    Fname=models.CharField(max_length=255)
    Mname=models.CharField(max_length=255)
    Lname=models.CharField(max_length=255)
    MobileNo=models.IntegerField()
    Email=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)
