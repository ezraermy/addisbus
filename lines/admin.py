from django.contrib import admin
from .models import BusStation, Line, Passengers

# Register your models here.

class LineAdmin(admin.ModelAdmin):
    pass 

class PassengersAdmin(admin.ModelAdmin):
    pass


admin.site.register(BusStation)

admin.site.register(Line, LineAdmin)  

admin.site.register(Passengers, PassengersAdmin)