from django.contrib import admin

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price', ]
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'paid_status', 'datetime_created']
    inlines = [OrderItemInline,]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price',]
