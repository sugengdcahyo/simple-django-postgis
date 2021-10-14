from django.contrib import admin
from annotations.models import WorldBorder

# Register your models here.
class WorldBorderAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lon')

admin.site.register(WorldBorder, WorldBorderAdmin)
