from django.db import models
from django.conf import settings
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=1000)
    paid_status = models.BooleanField(default=False)

    order_note = models.CharField(max_length=700, blank=True)
    
    datetime_created = models.DateField(auto_now_add=True)
    datetime_modified = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"Order {self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"Order Items:{self.id}: {self.product}x{self.quantity} Price:{self.price}"
    