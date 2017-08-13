from django.contrib import admin
from products.models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('collection', 'section')

admin.site.register(Section)
admin.site.register(Collection)
admin.site.register(Product, ProductAdmin)
