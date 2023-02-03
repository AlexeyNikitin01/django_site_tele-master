from django.shortcuts import render

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created_send_mail
from main.models import TVSale


def order_create_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if request.user.is_authenticated:
                user = request.user
            else:
                user = ''
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price_tv=item['price_tv'],
                    quantity=item['quantity'],
                    user_order=user,
                    # model_tv=item['model_tv']
                )
            cart.clear()
            order_created_send_mail(order.pk)
            return render(request, 'order_created.html',
                          {'cart': cart,
                           'order': order
                           })
    else:
        form = OrderCreateForm
    return render(request, 'order_create.html',
                  {'cart': cart, 'form': form})


def user_store_order_view(request):
    user_products = OrderItem.objects.filter(user_order=request.user)
    context = {
        'user_products': user_products,
    }
    return render(request, 'user_store_order.html', context)
