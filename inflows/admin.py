from django.contrib import admin
from . import models

class InflowsAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'description', 'created_at', 'updated_at')
    search_fields = ('supplier__name', 'product__name',)

admin.site.register(models.Inflows, InflowsAdmin)



