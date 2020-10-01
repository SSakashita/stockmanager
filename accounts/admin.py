from django.contrib import admin

from stock.models import Item, Category

admin.site.register(Item)
admin.site.register(Category)