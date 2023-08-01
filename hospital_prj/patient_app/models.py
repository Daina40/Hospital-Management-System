from django.db import models
from dr_details_app.models import Doctors
from hospital_app.models import Hospital

# Create your models here.
class Patients(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    specialized = models.CharField(max_length=200, null=True)
    patient_name = models.CharField(max_length=100)
    patient_age = models.CharField(max_length=20)
    patient_contact = models.CharField(max_length=20)
    appointment_sl = models.IntegerField(blank=True, null=True)
    appointment_date = models.DateTimeField(auto_now_add=True, null=True)
    
