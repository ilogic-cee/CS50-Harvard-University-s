from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    title =models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=1000)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner models.ForeighKey(User, on_delete=models.CASCADE, blank=true, null=true, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=true, null==true, related_name="category")
