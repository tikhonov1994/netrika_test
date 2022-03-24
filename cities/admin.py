from django.contrib import admin

from cities.models import Citizen, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    pass
