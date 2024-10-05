from django.shortcuts import render, redirect
from .form import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _
from cart.cart import Cart
from .models import OrderItem
# Create your views here.
@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, _("Your cart is empty"))
        return redirect('product_list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:                
                product = item['product_obj']
                OrderItem.objects.create(
                    order = order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price,
                )
            messages.success(request, _("Your order has submited succesfully"))

            cart.clear()
            request.user.firstname = order_obj.first_name
            request.user.lastname = order_obj.last_name
            request.user.save()
            

    return render(request, 'orders/order_form.html', context={
        "form":order_form,
    })