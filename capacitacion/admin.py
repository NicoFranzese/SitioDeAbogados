from django.contrib import admin
from .models import Capacitacion

# Register your models here.
class CapacitacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Capacitacion, CapacitacionAdmin)