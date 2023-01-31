from django.contrib import admin

# Register your models here.
from .models import Sensor,Measurement
# Register your models here.


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor_id', 'temperature','created_at']