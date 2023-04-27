

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .factory import ProductFactory
from .models import GiftWrap
from .salesperson import Salesperson
from .cart import Cart

def product_list(request):
    """
    View that displays a list of products.
    """
    factory = ProductFactory()

    salesperson = Salesperson("cart")
    # salesperson.update(add_product)

    products = [
        factory.create_product('TV'),
        GiftWrap(factory.create_product('Smartphone')),
        GiftWrap(factory.create_product('Speakers')),
    ]

    if request.method == 'POST':
        # Get the selected product from the form data
        add_product_name = request.POST.get('product')

        # Find the selected product object in the products list
        add_product = None
        for product in products:
            if product.get_name() == add_product_name:
                add_product = product
                break

        # Create a cart object for this session if it doesn't already exist
        if 'cart' not in request.session:
            request.session['cart'] = []

        # Add the selected product to the cart
        cart = Cart()
        cart.add_product(add_product)

    template = loader.get_template('pos_app_name/product_list.html')

    context = {
        'products': products,
    }

    return HttpResponse(template.render(context, request))


