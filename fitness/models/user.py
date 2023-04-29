from django.db import models

# creating the users

class User(models.Model):
    username = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)