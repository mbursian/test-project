from django.contrib import admin
from .models import *


class WeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in We._meta.fields]

    class Meta:
        model = We


admin.site.register(We, WeAdmin)