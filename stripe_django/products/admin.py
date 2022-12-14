from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    search_fields = ('id', 'name', 'price')
    list_filter = ('id', 'name', 'price')
