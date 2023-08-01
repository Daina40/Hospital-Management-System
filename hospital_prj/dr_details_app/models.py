from django.db import models

from hospital_app.models import Hospital

# Create your models here.
class Doctors(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    dr_name = models.CharField(max_length=100)
    specialized = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    def __str__(self):
        return self.dr_name
    
