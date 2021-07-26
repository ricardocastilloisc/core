from django.contrib import admin

from .models import Blue

@admin.register(Blue)
class BlueAdmin(admin.ModelAdmin):
    pass
