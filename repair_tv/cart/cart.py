from decimal import Decimal
from django.conf import settings

from main.models import TVSale


class Cart:
    def __init__(self, request):
        """
        Initial cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add product in cart or update quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price_tv': str(product.price_tv)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        """
        Remove product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iteration elements in cart and take product from database
        """
        product_ids = self.cart.keys()
        products = TVSale.objects.filter(id__in=product_ids)  # ???
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price_tv'] = Decimal(item['price_tv'])
            item['total_price_tv'] = item['price_tv'] * item['quantity']
            yield item

    def __len__(self):
        """
        Summa all products in cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Cost product in cart
        """
        return sum(Decimal(item['price_tv'])*item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
