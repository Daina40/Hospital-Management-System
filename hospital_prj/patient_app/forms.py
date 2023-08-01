from django import forms
from .models import Patients
from hospital_app.models import Hospital
from dr_details_app.models import Doctors

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patients
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hospital'].empty_label = "--SELECT--"        
        self.fields['hospital'].queryset = Hospital.objects.all()
        self.fields['doctor'].empty_label = "--SELECT--"        
        self.fields['doctor'].queryset = Doctors.objects.all()       