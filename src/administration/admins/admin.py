from django.contrib import admin
from .models import (
    Package, Purchase
)


class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'tokens', 'created_on', 'is_active']


class PurchaseAdmin(admin.ModelAdmin):
    list_filter = ['package', 'payment_method']
    list_display = ['user', 'package', 'amount_total', 'amount_paid', 'payment_method', 'tokens', 'created_on', 'is_active']


admin.site.register(Package, PackageAdmin)
admin.site.register(Purchase, PurchaseAdmin)
