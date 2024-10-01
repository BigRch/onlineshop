from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    favorites = models.ManyToManyField(Product, related_name='favorited', blank=True)