from django.contrib import admin
from .models import Product, Comment

class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'body', 'points', 'active', ]
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active',]
    inlines = [CommentsInline,]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'date_created', 'points', 'active', ]