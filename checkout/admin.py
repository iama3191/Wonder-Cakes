from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
        )

    fields = (
        'order_number',
        'user_profile',
        'full_name',
        'email',
        'phone_number',
        'country',
        'county',
        'city',
        'postcode',
        'street_address1',
        'street_address2',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',)

    list_display = (
        'order_number',
        'full_name',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
