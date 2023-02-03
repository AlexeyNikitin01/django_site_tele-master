from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'surname', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'date_created']
    list_filter = ['paid', 'date_created']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
