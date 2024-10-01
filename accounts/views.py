from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from products.models import Product

@login_required
def add_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    user.favorites.add(product)
    return redirect('product_list')

@login_required
def remove_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    user.favorites.remove(product)
    return redirect('product_list')
