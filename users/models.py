from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):


    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.TextField(max_length=255, blank=False)
    last_name = models.TextField(max_length=255,blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    position = models.TextField(max_length=255, blank=False)
    email = models.EmailField( max_length=254)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
     
