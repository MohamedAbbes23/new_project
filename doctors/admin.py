from django.contrib import admin
from .models import Doctor,Appointment, Patient

admin.site.register(Doctor)
admin.site.register(Patient)



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'appointment_date', 'appointment_time', 'description')

