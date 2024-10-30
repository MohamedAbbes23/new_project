from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Patient(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_history = models.TextField()
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name    
    


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateField(unique=True)  # Ensures that the date is not booked twice
    appointment_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Appointment with {self.patient_name} on {self.appointment_date} at {self.appointment_time}"


