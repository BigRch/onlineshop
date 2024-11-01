from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns =[
    path('admin/', admin.site.urls), 
    path('',views.HomePageView.as_view(), name= 'home'),
    path('aboutus', views.AboutusPageView.as_view(), name= 'aboutus'),
    path ('wishlist/', views.WishListView.as_view(), name='wishlist')
    ]