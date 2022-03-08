from django.contrib import admin

from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')


admin.site.register(Address, AddressAdmin)
