from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
# admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# Register your models here.
admin.site.register(Flight, FlightAdmin)