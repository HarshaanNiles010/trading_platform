from django.db import models

# Create your models here.
class Users(models.Model):
    fist_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,default=f'john.doe@gmail.com')