from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _
from .cart import Cart
from products.models import Product
from .forms import AddToCartProductForm
# Create your views here.

def cart_detail_view(request):
    cart =  Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inpalce': True,
        })

    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
    })
@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleand_data = form.cleaned_data
        quantity = cleand_data['quantity']
        cart.add(product, quantity, replace_quantity=cleand_data['inpalce'],)
    return redirect('product_list')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')

def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _("Your cart has cleared successfully"))
    else:
        messages.success(request, _("Your cart is empty already"))
    
    return redirect('cart:cart_detail')