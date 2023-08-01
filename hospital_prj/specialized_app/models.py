from django.db import models
from dr_details_app.models import Doctors
from hospital_app.models import Hospital

# Create your models here.
class Speciality(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    specialize_on = models.CharField(max_length=400)
    def __str__(self):
        return self.specialize_on