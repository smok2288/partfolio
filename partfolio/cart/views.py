from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from market.models import Product
from .cart import Cart
from .forms import CartForm
from coupons.forms import CouponApplyForm


@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartForm(initial={'quantity':item['quantity'], 'update':True})
    coupon_apply_form = CouponApplyForm()
    context = {'cart': cart, 'coupon_apply_form': coupon_apply_form}
    return render(request, 'detail.html', context)

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart')