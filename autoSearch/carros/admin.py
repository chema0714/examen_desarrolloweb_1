# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ["make","Type","year","colour","price","created"]
    searchfield = ["make","Type","year","colour"]
    list_filter = ["price"]

    class Meta:
        Model = Car
admin.site.register(Car, CarAdmin)
