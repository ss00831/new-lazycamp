from django.contrib import admin
from .models import Order, OrderLineItem

# Model fields displays in orders in Chexkout admin.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'user_profile', 'date',
                       'night_cost', 'order_total',
                       'original_book', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'night_cost', 'order_total',
              'original_book', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'night_cost',
                    'grand_total',
                    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
