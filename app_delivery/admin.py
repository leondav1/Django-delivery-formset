from django.contrib import admin

from app_delivery.models import Delivery, Address, File


class FileStackedInline(admin.StackedInline):
    max_num = 1


class DeliveryAddressInLine(admin.StackedInline):
    model = Address


class DeliveryFileInLine(FileStackedInline):
    model = File


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    inlines = [DeliveryFileInLine, DeliveryAddressInLine]
    list_display = ['title', 'product_type', 'delivery_date']
    search_fields = ('title', 'product_type')
    readonly_fields = ['created_at']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['delivery', 'addr']
    list_filter = ['delivery']
    search_fields = ('delivery__title', )
    readonly_fields = ['delivery']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['delivery', 'name']
    list_filter = ['delivery']
    search_fields = ('delivery__title', 'name')
    readonly_fields = ['delivery']
