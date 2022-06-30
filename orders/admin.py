from django.contrib import admin
from .models import Order, OderItem

# Register your models here.

admin.site.register(Order)
admin.site.register(OderItem)