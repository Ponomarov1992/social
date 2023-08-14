from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass


class Users(models.Model):
    first_name = models.CharField(max_length = 20, blank=False)
    last_name = models.CharField(max_length = 30, blank=False)
    full_name = models.CharField(max_length = 30, blank=False)
    phone_namber = models.IntegerField(max_length = 15, blank=False)
    about_me = models.CharField(max_length = 500, blank=False)
    age = models.IntegerField(max_length = 3, blank=False)
    
