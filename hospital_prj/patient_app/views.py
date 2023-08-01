from django.shortcuts import render, redirect
from django.contrib import messages
from patient_app.forms import PatientForm
from .models import *

# Create your views here.

def patient_details(request):
    patient = Patients.objects.all()
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Patient appointment added successfully")

    context = {
        'form' : form,
        'patient' : patient
    }
    
    return render(request, 'patient.html', context)

def patient_delete_item(request, id):
    patient = Patients.objects.get(id=id)
    patient.delete()
    messages.info(request, "Item deleted success")
    return redirect('patient_details')

def patient_edit_item(request, id):
    patients = Patients.objects.all()
    patient = Patients.objects.get(id=id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.info(request, "Patient updated successfully")
            return redirect('patient_details')

    else:
        form = PatientForm(instance=patient)

    context = {
        'form': form,
        'patients' : patients
    }
    return render(request, 'patient_edit.html', context)