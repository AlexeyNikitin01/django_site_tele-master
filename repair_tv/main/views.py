from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import login, authenticate

from .tasks import repair_order_send_mail
from .forms import RepairOrderForm
from .models import TVSale

from cart.forms import CartAddProductForm
from tm_user.forms import UserSignUpForm, UserSignInForm


def index(request):
    return render(request, template_name='main/index.html')


def about_site_tm(request):
    return render(request, template_name='main/about_site_tm.html')


def contact(request):
    return render(request, template_name='main/contact.html')


def price(request):
    return render(request, template_name='main/price.html')


def buy_tv(request):
    return render(request, template_name='main/sale_tvs.html')


def order_done(request):
    return render(request, 'main/order_done.html')


def repair_order(request):
    form = RepairOrderForm()
    if request.method == 'POST':
        form = RepairOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            repair_order_send_mail(order.pk)
            return redirect('order_done/')
        else:
            contex = {'form': form}
            return render(request, 'main/repair_order.html', contex)
    contex = {
        'form': form,
    }
    return render(request, 'main/repair_order.html', contex)


def sale_tvs(request):
    tvs = TVSale.objects.all()
    contex = {
        'tvs': tvs,
    }
    return render(request, 'main/sale_tvs.html', contex)


def sale_tv(request, pk, slug_tv):
    product = get_object_or_404(TVSale, pk=pk, slug_tv=slug_tv)
    cart_product_form = CartAddProductForm()
    contex = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'main/sale_tv.html', contex)
