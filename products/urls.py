from django.urls import path, include
from . import views
from accounts import views as accountviews
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('products/<int:product_id>/add_favorite', accountviews.add_favorite, name='add_favorite'),
    path('products/<int:product_id>/remove_favorite', accountviews.remove_favorite, name='remove_favorite'),
]
