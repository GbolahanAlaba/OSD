from django.contrib import admin
from .models import *
from .forms import *

class INV(admin.ModelAdmin):
    form = INVForm
    list_display = ['Product', 'Category', 'Quantity', 'Date', 'Vendor']
    list_filter = ['Product']
    search_fields = ['Product', 'Quantity']


admin.site.register(Sign_Up)
admin.site.register(Inventory, INV)




# Register your models here.
