from django import forms
from .models import Doctors
from hospital_app.models import Hospital

class DoctorCreateForm(forms.ModelForm):
    
    class Meta:
        model = Doctors
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hospital'].empty_label = "--SELECT--"        
        self.fields['hospital'].queryset = Hospital.objects.all()     