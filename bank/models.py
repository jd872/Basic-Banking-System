from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True,default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
