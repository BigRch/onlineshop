from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    # cover = models.ImageField()

    datetime_creation = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):

    PRODUCT_POINT = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    points = models.CharField(max_length=10, choices=PRODUCT_POINT)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("product_detail", args= [self.product.id])
    