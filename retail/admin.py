from django.contrib import admin
from retail.models import *

# Register your models here.

class PartnerAdmin(admin.ModelAdmin):
    list_filter = ('city','show','frontpage')

admin.site.register(City)
admin.site.register(Partner, PartnerAdmin)
