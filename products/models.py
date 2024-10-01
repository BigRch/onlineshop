from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    short_description = models.CharField(max_length=300, blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_("Product Image"), upload_to='product/product_cover/', blank=True)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)
    datetime_creation = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):

    PRODUCT_POINT = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_("Comment Field"))
    points = models.CharField(max_length=10, choices=PRODUCT_POINT, verbose_name=_("What is your assessment?"))

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("product_detail", args= [self.product.id])
    