from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    titile =models.CharField(max_length=300)
    description - models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=1000)
    price models.FloatField()
    isActive = models.BooleanField(default=time)
    owner models.ForeighKey(User, on_delete)
