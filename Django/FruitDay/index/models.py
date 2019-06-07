from django.db import models

# Create your models here.

class Users(models.Model):
    uphone = models.CharField(max_length=11)
    upwd = models.CharField(max_length=50)
    uemail = models.EmailField()
    uname = models.CharField(max_length=30)
    isActive = models.BooleanField(default=True)
