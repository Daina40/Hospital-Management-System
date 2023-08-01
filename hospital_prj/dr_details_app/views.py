from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import DoctorCreateForm

# Create your views here.
def dr_details(request):
    doctor = Doctors.objects.all()
    form = DoctorCreateForm()

    if request.method == 'POST':
        form = DoctorCreateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Doctor is added")

    context = {
        'form' : form,
        'doctor' : doctor
    }
    
    return render(request, 'dr_details.html', context)

def dr_delete_item(request, id):
    doctor = Doctors.objects.get(id=id)
    doctor.delete()
    messages.info(request, "Item deleted success")
    return redirect('dr_details')

def dr_edit_item(request, id):
    doctors = Doctors.objects.all()
    doctor = Doctors.objects.get(id=id)

    if request.method == 'POST':
        form = DoctorCreateForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.info(request, "Doctor updated successfully")
            return redirect('dr_details')

    else:
        form = DoctorCreateForm(instance=doctor)

    context = {
        'form': form,
        'doctors' : doctors
    }
    return render(request, 'dr_edit.html', context)





