from django import forms
from .models import Patient, Appointment

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'medical_history', 'contact_info']




class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'appointment_date', 'appointment_time', 'description']



class PrescriptionForm(forms.Form):
    patient_name = forms.CharField(max_length=100, label="Patient Name")
    medicines = forms.CharField(widget=forms.Textarea, label="List of Medicines")
    doctor_notes = forms.CharField(widget=forms.Textarea, required=False, label="Doctor Notes")

