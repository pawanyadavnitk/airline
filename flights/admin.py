from django.contrib import admin

from .models import Flight, Airport, Passenger

# to modify how the Flight model should be displayed on admin page
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    # list_display = ("__str__", "duration")

# Register your models here.
admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger)
