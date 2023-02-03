from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .tasks import repair_order_send_mail
from .forms import RepairOrderForm
from .models import TVSale

from cart.forms import CartAddProductForm
from comment.forms import CommentForm

from comment.models import Comment


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
    paginator = Paginator(tvs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contex = {
        'results': page_obj,
        'count': paginator.count,
    }
    return render(request, 'main/sale_tvs.html', contex)


class SaleTVView(View):
    def get(self, request, pk, slug_tv, *args, **kwargs):
        product = get_object_or_404(TVSale, pk=pk, slug_tv=slug_tv)
        cart_product_form = CartAddProductForm()
        comment_form = CommentForm()
        contex = {
            'product': product,
            'cart_product_form': cart_product_form,
            'comment_form': comment_form,
        }
        return render(request, 'main/sale_tv.html', contex)

    def post(self, request, pk, slug_tv):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['comment']
            username = self.request.user
            product = get_object_or_404(TVSale, pk=pk, slug_tv=slug_tv)
            comment = Comment.objects.create(com_to_model=product, username=username, comment=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        contex = {
            'comment_form': comment_form,
        }
        return render(request, 'main/sale_tv.html', contex)
