from django.contrib import admin
from .models import RepairOrder
from .models import TVSale


class RepairOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'description')
    list_filter = ['date_order']
    ordering = ['-date_order']
    search_fields = ['name', 'surname']


class SaleTVAdmin(admin.ModelAdmin):
    list_display = ('model_tv', 'price_tv', 'description_tv')
    list_filter = ['date_add', 'model_tv']
    ordering = ['-date_add', 'model_tv']
    search_fields = ['model_tv']
    prepopulated_fields = {"slug_tv": ("model_tv",)}


admin.site.register(RepairOrder, RepairOrderAdmin)
admin.site.register(TVSale, SaleTVAdmin)
